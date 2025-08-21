import streamlit as st
import requests
from streamlit_option_menu import option_menu
from pages.utils.helpers import capitalize_first

# ---- Inicialización de session_state ----
def init_auth_state():
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'token' not in st.session_state:
        st.session_state.token = None
    if 'show_auth' not in st.session_state:
        st.session_state.show_auth = False
    if 'username' not in st.session_state:
        st.session_state.username = None

# ---- API helpers ----
def authenticate(username, password):
    url_api = "http://127.0.0.1:8000/user-service/users/authenticate/"
    data = {'username': username, 'password': password}
    try:
        response = requests.post(url_api, data=data)
        if response.status_code == 200:
            return response.json().get('token')
        else:
            st.error("Authentication Error.")
    except Exception as e:
        st.error(f"Connection Error: {e}")
    return None

def register(username, email, password):
    url_api = "http://127.0.0.1:8000/user-service/users/"
    data = {'username': username, 'email': email, 'password': password}
    try:
        response = requests.post(url_api, data=data)
        if response.status_code == 201:
            return response.json()
        elif response.status_code == 400:
            error_message = parse_error_message(response)
            st.error(f"User Registration Error: {error_message}")
        else:
            st.error("User Registration Error.")
    except Exception as e:
        st.error(f"Connection Error: {e}")
    return None

def parse_error_message(response):
    try:
        error_data = response.json()
        if 'email' in error_data:
            return capitalize_first(error_data['email'][0])
        elif 'username' in error_data:
            return capitalize_first(error_data['username'][0])
        else:
            return "Unknown error while registering user."
    except:
        return "Unknown error while registering user."

# ---- Auth form ----
def auth_form():
    selected_option = option_menu(
        menu_title="Authentication",
        options=["Sign In", "Sign Up"],
        icons=["sign-in", "user-add"],
        menu_icon="lock",
        default_index=0,
        orientation="horizontal",
    )
    if selected_option == "Sign In":
        st.subheader("Sign In")
        username = st.text_input("Username", key="login_username")
        password = st.text_input("Password", type="password", key="login_password")
        if st.button("Sign In", key="btn_signin"):
            token = authenticate(username, password)
            if token:
                st.session_state.username = capitalize_first(username)
                st.session_state.token = token
                st.session_state.authenticated = True
                st.session_state.show_auth = False
                st.experimental_rerun()
            else:
                st.error("Sign In failed")
    else:
        st.subheader("Sign Up")
        username = st.text_input("Username", key="reg_username")
        email = st.text_input("Email", key="reg_email")
        password = st.text_input("Password", type="password", key="reg_password")
        repeat_password = st.text_input("Repeat Password", type="password", key="reg_repeat_password")
        if st.button("Sign Up", key="btn_signup"):
            if password == repeat_password and password != "":
                response = register(username, email, password)
                if response:
                    st.session_state.username = capitalize_first(username)
                    st.session_state.authenticated = True
                    st.session_state.token = response.get('token')
                    st.success("You have signed up successfully!")
                    st.success(f"You have automatically logged in. Welcome {st.session_state.username}!")
                    st.session_state.show_auth = False
                    st.experimental_rerun()
                else:
                    st.error("Sign Up failed")
            else:
                st.error("Passwords do not match.")

# ---- Bloque para el sidebar ----
def show_sidebar_auth():
    init_auth_state()
    with st.sidebar:
        if st.session_state.authenticated:
            st.success(f"Welcome back {st.session_state.username}!")
            if st.button("Log Out"):
                st.session_state.authenticated = False
                st.session_state.token = None
                st.experimental_rerun()
        else:
            if st.button("Sign In / Sign Up"):
                st.session_state.show_auth = not st.session_state.show_auth
            if st.session_state.show_auth:
                auth_form()
