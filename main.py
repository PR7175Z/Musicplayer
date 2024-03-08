import streamlit as st
import streamlit.components.v1 as components
from streamlit.components.v1 import html
import login
from seleniumfn import stream, stop
from function import *
import signup

loggedin = False

header()

status = login.login()
# print(status)
signup_button = st.button('Sign Up')
if signup_button:
    signup.signup()

if status:
    with st.form('searchform'):
        row2col1, row2col2 = st.columns([0.8, 0.2])
        with row2col1:
            inp = st.text_input(' ', placeholder='Search Here...')
        with row2col2:
            submitted = st.form_submit_button('Search')

    data_url = gifload("assets/images/music.gif")

    if submitted:
        running = stream(inp)
        if running:
            st.markdown(f'<img src="data:image/gif;base64,{data_url}" class="gifimg" alt="musicgif">',unsafe_allow_html=True)
            st.button('Stop', on_click=stop)

    