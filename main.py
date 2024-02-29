import streamlit as st
import streamlit.components.v1 as components
from streamlit.components.v1 import html
import base64
from function import stream, stop

def gifload(path):
    file_ = open(path, "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    return data_url

st.markdown(
    '''
    <style>
        button[title="View fullscreen"]{
            visibility: hidden;
        }
        .gifimg{
            width: 500px;
        }
    </style>
    ''',unsafe_allow_html=True
)

row1col1, row1col2 = st.columns([0.1, 0.9])
with row1col1:
    st.image("assets/images/logo.png", width=64)
with row1col2:
    st.markdown('<h1 class="pagetitle">Music Player</h1>',
                unsafe_allow_html=True)

with st.form('my_form'):
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

# file_ = open("assets/images/music.gif", "rb")
# contents = file_.read()
# data_url = base64.b64encode(contents).decode("utf-8")
# file_.close()

    