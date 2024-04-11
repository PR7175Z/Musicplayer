import streamlit as st
from seleniumfn import *
from function import *

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