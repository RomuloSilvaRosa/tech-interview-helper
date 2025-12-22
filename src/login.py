import streamlit as st

USERS = {
    "admin": "admin123",
    "interviewer": "interview123"
}

def login_page():
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USERS and USERS[username] == password:
            st.session_state.authenticated = True
            st.session_state.user = username
            st.rerun()
        else:
            st.error("Invalid credentials")
