import streamlit as st
import streamlit.components.v1 as components
from streamlit.components.v1 import html
import base64


row1col1, row1col2 = st.columns([0.1, 0.9])
with row1col1:
    st.image("assets/images/logo.png", width=64)
with row1col2:
    st.markdown('<h1 class="pagetitle">Music Player</h1>',
                unsafe_allow_html=True)

with st.form('my_form',clear_on_submit=False):
    uname = st.text_input(' ', placeholder='Username', max_chars=10)
    password = st.text_input(' ', placeholder='Password', type="password")
    submitted = st.form_submit_button('Submit')

if submitted:
    if len(uname)==0:
        st.write('Username field is empty')
    if len(password)==0:
        st.write('Password field is empty')
    print(uname, password)


    