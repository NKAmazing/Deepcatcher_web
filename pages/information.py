import streamlit as st
from pages.utils.auth import show_sidebar_auth
from pages.utils.footer import footer

# Set the page configuration
st.set_page_config(page_title="About Deepcatcher", page_icon="📄", initial_sidebar_state="expanded", layout="wide")

# Show the login sidebar
show_sidebar_auth()

def about():
    st.title("About Deepcatcher")

    # # Border top
    # st.markdown("---")

    # Introducción
    st.markdown(
        """
        ## Introduction
        Deepcatcher is an innovative solution aimed at combating the growing threat of deepfake technology. By leveraging advanced machine learning algorithms, Deepcatcher provides users with the tools they need to identify and report manipulated images effectively.
        """
    )

    # Border bottom
    st.markdown("---")

    # Sección de Información General (Abstract)
    st.markdown(
        """
        ## Abstract
        **Deepcatcher** is a software solution designed to detect images manipulated with Artificial Intelligence, commonly referred to as Deepfakes. The application employs a robust Machine Learning model to provide accurate predictions of image authenticity. Users interact with Deepcatcher through a responsive web interface, where they can upload images for analysis.

        The application also incorporates a user registration system, enabling users to log in, save their prediction results, and submit feedback or reports on the predictions made. This comprehensive approach ensures not only high accuracy in detecting fake images but also a user-friendly experience that facilitates ongoing interaction and improvement through user feedback. The combination of advanced AI techniques and a simplified web interface positions Deepcatcher as a valuable tool in the fight against digital image manipulation.
        """
    )

    # Border top
    st.markdown("---")

    # Sección de Arquitectura
    st.markdown("""
        ## Architecture Overview
        The architecture of Deepcatcher is designed to facilitate efficient image analysis and user interaction. It consists of three main modules: Backend, AI Model, and Frontend. Each module plays a crucial role in the overall functionality of the application. The following diagram illustrates the interactions between these modules, showcasing the flow of data and the relationships that enable Deepcatcher to function effectively.
    """)

    # Module selector
    options = ["Backend", "AI Model", "Frontend"]
    selection = st.radio("Select a module:", options, horizontal=True)

    if selection == "Backend":
        st.image("./static/backend_diagram.png", caption="REST API Diagram", width=300, clamp=True)
        st.markdown("""
        #### Backend
        The Backend is the part of the application that handles the server-side logic. It is responsible for managing the application's data and logic. 
        
        It consists of several key components:
        - **REST API with Django**: The Backend is built using the Django framework, providing a RESTful API to manage the main functionalities of the application.
        - **User Registration Tool**: Allows the creation and management of user accounts.
        - **Prediction History Tool**: Records and allows the consultation of predictions made by users.
        - **User Reporting Tool**: Users can make reports related to the predictions or any other aspect of the application.
        - **SQL Database**: User data, predictions, and reports are stored in an SQL database, ensuring data persistence and accessibility.
        """)
    elif selection == "AI Model":
        st.image("static/aimodel_diagram.png", caption="AI Detection Model Diagram", width=300, clamp=True)
        st.markdown("""
        #### AI Detection Model
        The AI Detection Model is the core component responsible for analyzing images and detecting deepfakes. It leverages advanced machine learning techniques to provide accurate predictions.

        It consists of several key components:
        - **Model Training**: The detection model is trained in a Python Notebook using TensorFlow, where a series of controlled steps are taken to train the deepfake detector.
        - **Direct Connection**: The detection model is loaded through a direct connection between the Frontend service and the model service. This is facilitated by TensorFlow tools that allow quick loading of a model in a Python script.
        """)
    elif selection == "Frontend":
        st.image("static/frontend_diagram.png", caption="Frontend Diagram", width=300, clamp=True)
        st.markdown("""
        #### Frontend
        The Frontend is the part of the application that users interact with. It is responsible for presenting the data and functionalities provided by the Backend and AI Model.

        It consists of several key components:
        - **Multi-page Interface with Streamlit**: The Frontend is developed with the Streamlit framework, which allows the rapid and easy creation of web interfaces.
            - **File Management Microservice**: Facilitates the management of files that users upload for predictions.
            - **Deepcatcher Web Pages**: Provide the user interface to interact with the various functionalities of the application, such as uploading files for detection, viewing prediction history, and reports.
        """)

    # Border bottom
    st.markdown("---")

    # Sección de Future Improvements
    st.markdown("""
    <style>
    .future-title {
        font-size: 2rem;
        font-weight: bold;
        margin-bottom: 0.2em;
    }
    .future-desc {
        font-size: 1rem;
        margin-bottom: 1.2em;
    }
    .improvement-list {
        display: flex;
        flex-direction: column;
        gap: 18px;
        margin-bottom: 32px;
    }
    .improvement-item {
        display: flex;
        flex-direction: row;
        align-items: stretch;
        border: 2px solid #222;
        border-radius: 14px;
        background: #fff;
        font-family: 'Comic Sans MS', 'Comic Sans', cursive;
        box-shadow: 2px 3px 0px 0px #bbb;
        overflow: hidden;
    }
    .improvement-name {
        background: #aee1fc;
        color: #222;
        min-width: 180px;
        max-width: 220px;
        font-weight: bold;
        font-size: 1.1rem;
        display: flex;
        align-items: center;
        justify-content: center;
        border-right: 2px solid #222;
        border-radius: 12px 0 0 12px;
        padding: 18px 12px;
        box-shadow: 2px 0 0 0 #bbb;
    }
    .improvement-desc {
        padding: 18px 18px;
        font-size: 1.05rem;
        color: #222;
        flex: 1;
        display: flex;
        align-items: center;
    }
    </style>

    <div class="future-title">Future Improvements</div>
    <div class="future-desc">
        The following improvements have been identified as valuable in the process of securing the information and preventing Fake News around the Internet. However, due to the complexity of their implementation and the high cost involved, these improvements are not feasible for the current version of Deepcatcher. We hope to address these in future updates.
    </div>
    <div class="improvement-list">
        <div class="improvement-item">
            <div class="improvement-name">Predictions in Videos</div>
            <div class="improvement-desc">
                Extend the detection model's capabilities to analyze entire videos, identifying segments manipulated with Deepfakes.
            </div>
        </div>
        <div class="improvement-item">
            <div class="improvement-name">Image Scanning</div>
            <div class="improvement-desc">
                Implement a feature that allows images to be scanned from mobile devices or cameras directly into the application for analysis.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Border bottom
    st.markdown("---")

    # Sección de Créditos
    st.markdown(
    """
## Credits
- **Developer**: [Nicolas Mayoral](https://github.com/NKAmazing), student at the Faculty of Engineering, Universidad de Mendoza
- **Specialist Tutor in Charge**: Mariela Asensio
- **University**: Universidad de Mendoza
    """
)

    # Sección de Footer
    footer()

if __name__ == "__main__":
    about()
