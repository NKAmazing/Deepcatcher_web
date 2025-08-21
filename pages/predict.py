import streamlit as st
from streamlit_option_menu import option_menu
import tensorflow as tf
import numpy as np
from PIL import Image
import requests
from streamlit_elements import elements, mui
from pages.utils.auth import show_sidebar_auth

# List of Model paths
model_paths = ['models/model_3.h5', 'models/model_4.h5', 'models/mobilenet_model.h5', 'models/xception_model.h5']

# Load the model
model_index = 3  # Cambiar este índice para elegir el modelo (lista model_paths)
model = tf.keras.models.load_model(model_paths[model_index])

# Definir el tamaño de entrada esperado según el modelo
if model_index in [2, 3]:  # mobilenet_model.h5 o xception_model.h5
    model_input_size = (224, 224)
else:  # model_3.h5 o model_4.h5
    model_input_size = (96, 96)

# Set the page configuration
st.set_page_config(page_title="Deepcatcher Demo - Prediction", page_icon=":computer:")

# Set the sidebar title
st.sidebar.title("Deepcatcher Demo")

# Set the options in the sidebar
options = st.sidebar.radio("Select an option: ", ["Predict Menu", "Tutorial"])

# Show the login sidebar
show_sidebar_auth()

# Function to preprocess the uploaded image
def preprocess_image(image, target_size):
    '''
    Function to preprocess the uploaded image for prediction
    params:
        image: Uploaded image
        target_size: Target size for the image
    '''
    try:
        # Open the image
        img = Image.open(image)

        # Convert to RGB (in case of alpha channel)
        img = img.convert("RGB")

        # Resize the image with the target size
        img = img.resize(target_size)

        # Convert to numpy array and normalize
        img = np.array(img) / 255.0

        # Expand the dimensions for the batch
        img = np.expand_dims(img, axis=0)

        return img
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None

# Function to perform prediction
def predict(image_data, model):
    '''
    Function to perform prediction on the image data using the model
    params:
        image_data: Preprocessed image data
        model: Trained model
    '''
    try:
        # Realizar la predicción
        prediction = model.predict(image_data)
        pred_values = tf.squeeze(prediction).numpy()

        # Si la salida es escalar (modelo binario)
        if np.isscalar(pred_values) or pred_values.shape == ():
            predicted_class = 'Real' if pred_values >= 0.5 else 'Fake'
            confidence = pred_values * 100 if predicted_class == 'Real' else (1 - pred_values) * 100
        else:
            # Multiclase (vector de probabilidades)
            classes = ['Fake', 'Real']
            idx = np.argmax(pred_values)
            predicted_class = classes[idx]
            confidence = pred_values[idx] * 100

        return predicted_class, confidence
    except Exception as e:
        st.error(f"Prediction Error: {str(e)}")
        return None, None

def get_user_id(token):
    '''
    Function to get the user ID from the API using the token
    params:
        token: Token of the authenticated user
    '''
    # Set the URL of the API
    url_api = "http://127.0.0.1:8000/user-service/user/id/"

    # Set the headers with the token
    headers = {'Authorization': f'Token {token}'}
    try:
        # Make the GET request to the API
        response = requests.get(url_api, headers=headers)

        # Check the status code of the response
        if response.status_code == 200:
            # If the response is successful, return the user ID
            return response.json().get('user_id')
        else:
            # If there is an error, display the error message
            st.error(f"Error at getting the User ID. Status Code: {response.status_code}")
            return None
    except Exception as e:
        st.error(f"Error at making the request: {str(e)}")
        return None

def save_prediction(user_id, predicted_class, confidence, image_file, token):
    '''
    Function to save the prediction result in the API
    params:
        user_id: User ID
        predicted_class: Predicted class of the image (Real/Fake)
        confidence: Confidence of the prediction
        image_file: Uploaded image file to save
        token: Token of the authenticated user
    '''
    # Set the URL of the API
    url_api = "http://127.0.0.1:8000/user-service/predictions/"

    # Set the headers with the token
    headers = {'Authorization': f'Token {token}'}

    # Set the data and files to send in the POST request
    files = {'image': image_file}
    data = {
        'predicted_class': predicted_class,
        'confidence': confidence,
        'user': user_id,
    }

    # Make the POST request to the API
    response = requests.post(url_api, headers=headers, data=data, files=files)

    # Check the status code of the response
    if response.status_code == 201:
        # If the response is successful, display the success message
        success_message = "Prediction successfully saved in the application."
        st.success(success_message)
    else:
        # If there is an error, display the error message
        error_message = f"Error at saving the prediction result: {response.status_code} - {response.json()}"
        st.error(error_message)

# ----------------------------------------------------------------------------------------------------------------
# Delete Functionality
# ----------------------------------------------------------------------------------------------------------------

def delete_prediction(prediction_id, token):
    ''' 
    Function to delete request to the API to delete a prediction
    params:
        prediction_id: Prediction ID to delete
        token: Token of the authenticated user
    '''
    # Set the URL of the API
    url_api = f"http://127.0.0.1:8000/user-service/predictions/{prediction_id}/"

    # Set the headers with the token
    headers = {'Authorization': f'Token {token}'}

    # Make the DELETE request to the API
    response = requests.delete(url_api, headers=headers)

    # Check the status code of the response
    if response.status_code == 204:
        return True, None  # Success, no error message
    else:
        return False, f"Error deleting the prediction: {response.status_code} - {response.json()}"

# Function to create a delete callback
def create_delete_callback(prediction_id, token, success_callback, error_callback):
    ''' 
    Define the callback function to set the prediction ID and 
    token and calls the delete_prediction function
    params:
        prediction_id: Prediction ID to delete
        token: Token of the authenticated user
        success_callback: Callback function to handle success message
        error_callback: Callback function to handle error message
    '''
    # Define the callback function
    def callback():
        # Call the delete prediction function
        success, error_message = delete_prediction(prediction_id, token)

        # Check if the deletion was successful
        if success:
            success_callback() # Call the success callback
        else:
            error_callback(error_message) # Call the error callback
    return callback

# ----------------------------------------------------------------------------------------------------------------
# Prediction History View
# ----------------------------------------------------------------------------------------------------------------

def get_prediction_history(user_id, token):
    '''
    Function to get request to the API to get the prediction history for a user
    params:
        user_id: User ID
        token: Token of the authenticated user
    '''
    # Set the URL of the API
    url_api = f"http://127.0.0.1:8000/user-service/predictions/?user={user_id}"

    # Set the headers with the token
    headers = {'Authorization': f'Token {token}'}

    # Make the GET request to the API
    response = requests.get(url_api, headers=headers)

    # Check the status code of the response
    if response.status_code == 200:
        # If the response is successful, return the predictions
        return response.json()
    else:
        # If there is an error, display the error message
        st.error(f"Error at getting predictions history for this user.")
        st.error(f"The Error was: {response.status_code} - {response.json()}")
        return []

def display_prediction_history(predictions, token):
    '''
    Display the prediction history in a card format 
    using Mui components of Streamlit-Elements
    params:
        predictions: List of prediction history
        token: Token of the authenticated user
    '''
    if predictions:
        st.subheader('Predictions History')

        # Set the elements container to display the history
        with elements("history"):

            # Sort by timestamp descending
            predictions = sorted(predictions, key=lambda x: x['timestamp'], reverse=True)  

            # Iterate over the predictions
            for prediction in predictions:

                # Ensure the ID is captured correctly
                prediction_id = prediction['id']  

                # Determine the color of the typography based on the predicted class
                color = "green" if prediction['predicted_class'] == 'Real' else "red"

                # Placeholder to display the prediction
                placeholder = st.empty()

                # Display the prediction in a card format
                with mui.Card(sx={"maxWidth": 700, "margin": "20px auto", "border-radius": 10, 
                                  "border": f"2px solid {color}", 
                                  "boxShadow": "0 0 10px rgba(0, 0, 0, 0.1)"}, 
                                  variant="outlined"):
                    # Card content
                    with mui.Grid(container=True, spacing=2):
                        # Display the image of the prediction
                        with mui.Grid(item=True, xs=12, sm=3):
                            mui.CardMedia(
                                component="img",
                                height="auto",
                                width="100%",
                                image=prediction['image'],  
                                alt="Image Prediction"
                            )
                        # Display the prediction details
                        with mui.Grid(item=True, xs=12, sm=8):
                            mui.CardContent(sx={"height": "100%"})(
                                # Showing Predicted Class
                                mui.Typography(
                                    f"{prediction['predicted_class']}",
                                    style={"fontSize": "1.5rem", "fontWeight": "bold", "color": color},
                                    variant="h5"
                                ),
                                mui.Divider(),
                                # Spacer
                                mui.Box(sx={"height": 10}),
                                mui.Typography(
                                    f"Confidence of {prediction['confidence']:.2f}%",
                                    style={"fontSize": "1rem", "fontWeight": "bold"}
                                ),
                                mui.Typography(
                                    # Separate the date and time
                                    f"Saved the date {prediction['timestamp'].split('T')[0]} at {prediction['timestamp'].split('T')[1].split('.')[0]}",
                                    style={"fontSize": "0.9rem"}
                                )
                            )
                    # Card actions
                    with mui.CardActions(sx={"display": "flex", "justifyContent": "space-between"}):
                        # Delete button for the prediction
                        mui.Button(
                            "Delete", 
                            size="small",
                            sx={"backgroundColor": "red", "color": "white", "marginLeft": "auto"},
                            onClick=create_delete_callback(prediction_id, token, 
                                               lambda: show_delete_success(placeholder), 
                                               lambda error_message: show_delete_error(placeholder, error_message))  # Use the callback function
                        )
    else:
        st.info('No hay predicciones disponibles.')

def show_delete_success(placeholder):
    '''
    Show success message after deleting a prediction
    '''
    # Display the success message after deleting the prediction
    with placeholder:
        with st.expander("Delete Status", expanded=True):
            st.success(f"Prediction successfully deleted.")

def show_delete_error(placeholder, error_message):
    '''
    Show error message after failed to delete a prediction
    '''
    # Display the error message after failing to delete the prediction
    with placeholder:
        with st.expander("Delete Status", expanded=True):
            st.error(f"Error deleting prediction: {error_message}")

def history_view():
    ''' 
    Prediction history view to display the prediction history 
    '''
    if 'authenticated' in st.session_state and st.session_state.authenticated:
        # Get the user ID
        user_id = get_user_id(st.session_state.token)

        # If the user ID is available
        if user_id:
            # Get the predictions of the user
            predictions = get_prediction_history(user_id, st.session_state.token)

            # Call the function to display the prediction history
            display_prediction_history(predictions, st.session_state.token)
        else:
            st.error('Unable to get the user ID.')
    else:
        st.warning('History is empty.')
        st.warning('Please login to view prediction history.')

# ----------------------------------------------------------------------------------------------------------------
# Prediction View
# ----------------------------------------------------------------------------------------------------------------

def predict_view():
    '''
    Prediction view to upload images and display the prediction result
    '''
    # Header title for the predict view
    st.header("Image Classification: Real vs. Fake")
    
    # Set the File Uploader
    uploaded_files = st.file_uploader("Choose images...", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

    if uploaded_files:
        # Set the number of columns per row
        cols_per_row = 3

        if len(uploaded_files) <= 2:
            cols = st.columns(len(uploaded_files))
            for i, uploaded_file in enumerate(uploaded_files):
                index = i
                image = preprocess_image(uploaded_file, target_size=model_input_size)
                if image is not None:
                    predicted_class, confidence = predict(image, model)
                    # Generar cartel HTML aquí
                    if predicted_class is not None:
                        if predicted_class == 'Real':
                            color = '#FFD600'
                            value_color = 'green'
                            value_text = 'REAL'
                        else:
                            color = '#FFD600'
                            value_color = 'red'
                            value_text = 'FAKE'
                        html = f'''
                        <div style="display: flex; justify-content: center;">
                            <span style="color: {color}; font-weight: bold; font-size: 1.1rem;">Predicción:&nbsp;</span>
                            <span style="color: {value_color}; font-weight: bold; font-size: 1.1rem;">{value_text}</span>
                        </div>
                        '''
                        cols[i].markdown(html, unsafe_allow_html=True)
                        # Mostrar imagen
                        cols[i].image(uploaded_file, use_column_width=True)
                        # Centrar el caption debajo de la imagen, solo texto color celeste
                        caption_html = f'''
                        <div style="display: flex; justify-content: center;">
                            <span style="color: #00B8D4; font-size: 1rem; margin-top: 8px;">
                                Uploaded Image ({predicted_class}, {confidence:.2f}%)
                            </span>
                        </div>
                        '''
                        cols[i].markdown(caption_html, unsafe_allow_html=True)
                        # Espacio visual entre el caption y el botón
                        cols[i].markdown('<div style="height: 18px;"></div>', unsafe_allow_html=True)
                        if len(uploaded_files) == 2:
                            # Centrar el botón usando subcolumnas
                            subcols = cols[i].columns([1, 2, 1])
                            with subcols[1]:
                                if st.button(f"Save Prediction {index+1}"):
                                    if 'authenticated' in st.session_state and st.session_state.authenticated:
                                        user_id = get_user_id(st.session_state.token)
                                        predictions = get_prediction_history(user_id, st.session_state.token)
                                        if len(predictions) >= 10:
                                            st.warning('You have reached the limit of 10 saved predictions.')
                                        else:
                                            with st.expander("Prediction Status", expanded=True):
                                                save_prediction(user_id, predicted_class, confidence, uploaded_file, st.session_state.token)
                                    else:
                                        st.warning('Please login to save the prediction.')
                        else:
                            subcols = cols[i].columns([3, 4, 1])
                            with subcols[1]:
                                if st.button(f"Save Prediction {index+1}"):
                                    if 'authenticated' in st.session_state and st.session_state.authenticated:
                                        user_id = get_user_id(st.session_state.token)
                                        predictions = get_prediction_history(user_id, st.session_state.token)
                                        if len(predictions) >= 10:
                                            st.warning('You have reached the limit of 10 saved predictions.')
                                        else:
                                            with st.expander("Prediction Status", expanded=True):
                                                save_prediction(user_id, predicted_class, confidence, uploaded_file, st.session_state.token)
                                    else:
                                        st.warning('Please login to save the prediction.')
        else:
            rows = (len(uploaded_files) + cols_per_row - 1) // cols_per_row
            for row in range(rows):
                cols = st.columns(cols_per_row)
                for col_index in range(cols_per_row):
                    index = row * cols_per_row + col_index
                    if index < len(uploaded_files):
                        uploaded_file = uploaded_files[index]
                        with cols[col_index]:
                            image = preprocess_image(uploaded_file, target_size=model_input_size)
                            if image is not None:
                                predicted_class, confidence = predict(image, model)
                                if predicted_class is not None:
                                    if predicted_class == 'Real':
                                        color = '#FFD600'
                                        value_color = 'green'
                                        value_text = 'REAL'
                                    else:
                                        color = '#FFD600'
                                        value_color = 'red'
                                        value_text = 'FAKE'
                                    html = f'''
                                    <div style="display: flex; justify-content: center;">
                                        <span style="color: {color}; font-weight: bold; font-size: 1.1rem;">Predicción:&nbsp;</span>
                                        <span style="color: {value_color}; font-weight: bold; font-size: 1.1rem;">{value_text}</span>
                                    </div>
                                    '''
                                    st.markdown(html, unsafe_allow_html=True)
                                    # Mostrar imagen
                                    st.image(uploaded_file, use_column_width=True)
                                    # Centrar el caption debajo de la imagen, solo texto color celeste
                                    caption_html = f'''
                                    <div style="display: flex; justify-content: center;">
                                        <span style="color: #00B8D4; font-size: 1rem; margin-top: 8px;">
                                            Uploaded Image ({predicted_class}, {confidence:.2f}%)
                                        </span>
                                    </div>
                                    '''
                                    st.markdown(caption_html, unsafe_allow_html=True)
                                    # Espacio visual entre el caption y el botón
                                    st.markdown('<div style="height: 18px;"></div>', unsafe_allow_html=True)
                                    # Centrar el botón usando subcolumnas
                                    subcols = st.columns([1,5,1])
                                    with subcols[1]:
                                        if st.button(f"Save Prediction {index+1}"):
                                            if 'authenticated' in st.session_state and st.session_state.authenticated:
                                                user_id = get_user_id(st.session_state.token)
                                                predictions = get_prediction_history(user_id, st.session_state.token)
                                                if len(predictions) >= 10:
                                                    st.warning('You have reached the limit of 10 saved predictions.')
                                                else:
                                                    with st.expander("Prediction Status", expanded=True):
                                                        save_prediction(user_id, predicted_class, confidence, uploaded_file, st.session_state.token)
                                            else:
                                                st.warning('Please login to save the prediction.')

# ----------------------------------------------------------------------------------------------------------------
# Tutorial Option
# ----------------------------------------------------------------------------------------------------------------

def tutorial_option():
    st.markdown(
            """
            ## Tutorial - Prediction

            Welcome to the Deepcatcher Demo Prediction page! Here you can upload images and get predictions on whether they are real or fake. Let's see a little guide on how to use this page.

            ### Instructions:
            1. **Select an Option**: Choose between the **Predict** option to upload images and get predictions, or the **History** option to view your prediction history.
            2. **Upload Images**: Click on the **Choose images...** button to upload images for prediction.
            3. **View Predictions**: After uploading images, you will see the prediction results displayed below each image.
            4. **Save Predictions**: You can save the prediction results by clicking the **Save Prediction** button below each image.
            5. **View History**: Click on the **History** option to view your saved predictions history.

            ### Note:
            - **Authentication**: To save predictions, you need to be logged in. Use the **User Authentication** option in the sidebar to sign in or sign up.
            - **Prediction Limit**: You can save up to 10 predictions. Once you reach the limit, you will not be able to save more predictions.

            ### Help Guide Video
            - Watch the video below to learn more about how to use the Deepcatcher Demo Prediction page.
                
            """
        )

    # Display the video
    st.video("https://youtu.be/O3HEp2P_MAk")

    st.markdown(
        """
        ### Get Started:
        - Choose the **Predict Menu** option to get started with image predictions!
        """
    )

# ----------------------------------------------------------------------------------------------------------------

# Main Streamlit app
def main():
    '''
    Main function to run the Streamlit page
    '''
    st.title("Deepcatcher Demo")

    # Check the selected option of the sidebar
    if options == "Predict Menu":
        # Show the prediction main menu
        selected_option = option_menu(
            menu_title="Prediction Main Menu",
            options=["Predict", "History"],
            icons=["camera", "clock"],  # optional
            menu_icon="cast",  # optional
            default_index=0,
            orientation="horizontal", # orientation: horizontal (default) or vertical
        )
        # Check the selected option of the menu
        if selected_option == "Predict":
            predict_view()
        elif selected_option == "History":
            history_view()
    elif options == "Tutorial":
        # Show the tutorial option
        tutorial_option()
    else:
        st.error("Invalid option selected.")

if __name__ == '__main__':
    main()