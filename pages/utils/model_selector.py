import streamlit as st

# List of Model paths
model_paths = ['models/model_3.h5', 'models/model_4.h5', 'models/mobilenet_model.h5', 'models/xception_model.h5']

models_options = {
    "MobileNet": model_paths[2],
    "Xception": model_paths[3],
}

def select_model(models=list(models_options.keys()), label="Select a model: ", index=0):
    """
    Muestra un selectbox para que el usuario elija un modelo.
    Devuelve el modelo seleccionado (string).
    """
    with st.sidebar:
        selected_model = st.selectbox(label, models, index=index)
    return selected_model

def load_model_path(selected_model):
    """
    Carga el modelo seleccionado.
    Devuelve la ruta del modelo seleccionado (string).
    """
    model_path = models_options.get(selected_model, model_paths[0])
    return model_path

def show_actual_model(selected_model):
    """
    Muestra el modelo actual seleccionado en el sidebar.
    """
    with st.sidebar:
        st.markdown(f"**Current Model:** {selected_model}")