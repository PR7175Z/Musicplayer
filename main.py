import streamlit as st
import streamlit.components.v1 as components
from streamlit.components.v1 import html
from streamlit_js_eval import streamlit_js_eval

from login import *
from seleniumfn import *
from function import *
from signup import *

st.set_page_config(
    page_title="Music Player",
    page_icon="🎵",
)

header()

def session_state():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
        # st.session_state.show_login = True
        # st.session_state.show_signup = False
        # st.session_state.signup_completed = False

session_state()

import time

if not st.session_state.logged_in:
    login()
    signup_button = st.button('Sign Up')

    if signup_button:
        st.session_state.show_login = False
        st.session_state.show_signup = True

    if st.session_state.show_signup:
        signup()
else:
    with st.form('searchform', clear_on_submit=False):
        row2col1, row2col2 = st.columns([0.8, 0.2])
        with row2col1:
            inp = st.text_input(' ', placeholder='Search Here...')
        with row2col2:
            searched = st.form_submit_button('Search')

    data_url = gifload("assets/images/music.gif")

    if searched:
        running = stream(inp)
        if running:
            st.write(f'Now playing: {get_name()}')
            st.write(f'Artist: {get_channel_name()}')
            st.write(f'Views: {get_views()}')
            st.write(f'Published: {get_date()}')
            st.markdown(f'<img src="data:image/gif;base64,{data_url}" class="gifimg" alt="musicgif">',unsafe_allow_html=True)
            # st.button('Next', on_click=getnextvideolink)
            st.button('Stop', on_click=pauseAndPlay)