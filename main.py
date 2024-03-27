import streamlit as st
import streamlit.components.v1 as components
from streamlit.components.v1 import html
from streamlit_js_eval import streamlit_js_eval

from login import *
from seleniumfn import *
from function import *
from signup import *

loggedin = False
st.set_page_config(
    page_title="Music Player",
    page_icon="🎵",
)

header()

login_placeholder = st.empty()
signup_clicked = False
with login_placeholder.container():
    status = login()
    signup_button = st.button('Sign Up')

if not status:
    if signup_button:
        login_placeholder.empty()
        signup()
        signup_clicked = True

if status:
    with st.form('searchform', clear_on_submit=False):
        row2col1, row2col2 = st.columns([0.8, 0.2])
        with row2col1:
            inp = st.text_input(' ', placeholder='Search Here...')
        with row2col2:
            searched = st.form_submit_button('Search')

        print(inp)

    data_url = gifload("assets/images/music.gif")

    if searched:
        print("working")
        running = stream(inp)
        if running:
            st.markdown(f'<img src="data:image/gif;base64,{data_url}" class="gifimg" alt="musicgif">',unsafe_allow_html=True)
            st.button('Stop', on_click=stop)

    
# with st.form('searchform', clear_on_submit=False):
#     row2col1, row2col2 = st.columns([0.8, 0.2])
#     with row2col1:
#         inp = st.text_input(' ', placeholder='Search Here...')
#     with row2col2:
#         searched = st.form_submit_button('Search')

# data_url = gifload("assets/images/music.gif")

# if searched:
#     running = stream(inp)
#     if running:
#         st.markdown(f'<img src="data:image/gif;base64,{data_url}" class="gifimg" alt="musicgif">',unsafe_allow_html=True)
#         st.button('Stop', on_click=stop)