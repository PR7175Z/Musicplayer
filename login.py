import streamlit as st
import streamlit.components.v1 as components
from streamlit.components.v1 import html

def login():
    with st.form('loginform',clear_on_submit=False):
        st.write("<h2>Login</h2>", unsafe_allow_html=True)
        uname = st.text_input(' ', placeholder='Username', max_chars=10)
        password = st.text_input(' ', placeholder='Password', type="password")
        submitted = st.form_submit_button('Submit')
        st.write("<a href='#' id='my-link'>Forgot Password</a>", unsafe_allow_html=True)

    if submitted:
        if len(uname)==0:
            st.write('Username field is empty')
        if len(password)==0:
            st.write('Password field is empty')
        print(uname, password)

if __name__ == "__main__":
    login()