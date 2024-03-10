import streamlit as st
import streamlit.components.v1 as components
from streamlit.components.v1 import html
from function import get_users
# import base64 

def login():
    corflag = 0
    with st.form('loginform',clear_on_submit=False):
        st.write("<h2>Login</h2>", unsafe_allow_html=True)
        email = st.text_input(' ', placeholder='Username', max_chars=60)
        password = st.text_input(' ', placeholder='Password', type="password")
        submitted = st.form_submit_button('Submit')
        st.write("<a href='#' id='my-link'>Forgot Password</a>", unsafe_allow_html=True)

    if submitted:
        if(len(email)==0 or len(password)==0):
            if len(email)==0:
                st.write('Username field is empty')
            if len(password)==0:
                st.write('Password field is empty')
        else:
            users = get_users()
            for x in users:
                if email == x[1] and password == x[2]:
                    # st.write('correct')
                    corflag = 1

                # st.write(x[1], x[2])
            if corflag==1:
                st.write('login successful')
                return True
            else:
                st.write('invalid credential')

if __name__ == "__main__":
    login()