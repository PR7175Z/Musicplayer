import streamlit as st
import streamlit.components.v1 as components
from streamlit.components.v1 import html
from function import get_users, decode_password
import time

def checkcredential(email,password):
    corflag = 0
    if(len(email)==0 or len(password)==0):
        if len(email)==0:
            st.write('Username field is empty')
        if len(password)==0:
            st.write('Password field is empty')
    else:
        users = get_users()
        for x in users:
            if email == x[1] and password == decode_password(x[2]):
                corflag = 1
    return corflag

    
def login():
    if st.session_state.show_login:
        corflag = 0
        with st.form('loginform',clear_on_submit=False):
            st.write("<h2>Login</h2>", unsafe_allow_html=True)
            email = st.text_input(' ', placeholder='Username', max_chars=60)
            password = st.text_input(' ', placeholder='Password', type="password")
            loggedin = st.form_submit_button('Submit')

        if loggedin:
            corflag = checkcredential(email, password)
            if corflag==1:
                st.session_state.logged_in = True
                st.success('Login Successful')
                time.sleep(1)
            else:
                st.error('The provided credentials are not correct')

if __name__ == "__main__":
    login()