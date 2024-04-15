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

hide_sidebar()

header()

def session_state():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

session_state()

tab1,tab2 = st.tabs(['Login', 'Sign up'])

with tab1:
    if not st.session_state.logged_in:
        login()
    else:
        nav_page('search')
with tab2:
    if not st.session_state.logged_in:
        signup()
    else:
        nav_page('search')