import streamlit as st
from login import login_page
from pillars import pillars_page

st.set_page_config(page_title="Interview Evaluation", layout="wide")

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    login_page()
else:
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Pillars Assessment"])

    if page == "Pillars Assessment":
        pillars_page()
