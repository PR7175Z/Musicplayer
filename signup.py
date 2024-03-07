import streamlit as st
import streamlit.components.v1 as components
from streamlit.components.v1 import html
from function import insert_user

def signup():
    with st.form('signupform',clear_on_submit=False):
        st.write("<h2>Sign Up</h2>", unsafe_allow_html=True)
        first_name = st.text_input(' ', placeholder='First Name', max_chars=20 )
        last_name = st.text_input(' ', placeholder='Last Name', max_chars=20 )
        email = st.text_input(' ', placeholder='Email', max_chars=80)
        password = st.text_input(' ', placeholder='Password', type="password")
        submitted = st.form_submit_button('Submit')
        
    st.button('Login')

    if submitted:
        if(len(email)==0 or len(password)==0 or len(first_name)==0 or len(last_name)==0):
            if len(email)==0:
                st.write('Username field is empty')
            if len(password)==0:
                st.write('Password field is empty')
        else:
            insert_user(first_name, last_name, email, password)
            st.write("login")
        

if __name__ == "__main__":
    signup()
    