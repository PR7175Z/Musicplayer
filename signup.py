import streamlit as st
import streamlit.components.v1 as components
from streamlit.components.v1 import html

def signup():
    with st.form('signupform',clear_on_submit=False):
        st.write("<h2>Sign Up</h2>", unsafe_allow_html=True)
        uname = st.text_input(' ', placeholder='Username', max_chars=10)
        password = st.text_input(' ', placeholder='Password', type="password")
        submitted = st.form_submit_button('Submit')
        
    st.button('Login')

    if submitted:
        if(len(uname)==0 or len(password)==0):
            if len(uname)==0:
                st.write('Username field is empty')
            if len(password)==0:
                st.write('Password field is empty')
        else:
            st.write("login")
        


    