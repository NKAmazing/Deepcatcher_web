import streamlit as st
from st_pages import Page, show_pages, add_page_title

# Set page configuration
st.set_page_config(page_title="Deepcatcher - A Deep Learning based Software Detection System", page_icon=":globe_with_meridians:", layout="wide", initial_sidebar_state="expanded")

st.title("Welcome to Deepcatcher Demo")

# Information about the project
st.write("Deepcatcher is a Deep Learning based Software Detection System that uses Convolutional Neural Networks to detect software in images.")
st.write("This project is a part of the course project for the course TIF III: Trabajo Integrador Final III at Universidad Nacional de Mendoza, Argentina.")

# Set the pages in the sidebar of the app
show_pages([
    Page("main.py", "Home", "🏠"),
    Page("pages/information.py", "About", "📖"),
    Page("pages/predict.py", "Predict", "🖥️"),
    Page("pages/authenticate.py", "Sign In/Sign Up", "🔒"),
    Page("pages/report.py", "Report", "📝"),
])


