import streamlit as st
from seleniumfn import *
from function import *
from datetime import datetime
import pandas as pd
import numpy as np

hide_sidebar()
header()

cur_userid = st.session_state.logged_in_id

tab1, tab2 = st.tabs(["Search", "History"])
with tab1:
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
            date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            name = get_name()
            st.write(f'Now playing: {name}')
            st.write(f'Artist: {get_channel_name()}')
            st.write(f'Views: {get_views()}')
            st.write(f'Published: {get_date()}')
            st.markdown(f'<img src="data:image/gif;base64,{data_url}" class="gifimg" alt="musicgif">',unsafe_allow_html=True)
            insert_history(cur_userid, name, date_time)
            st.button('Stop', on_click=pauseAndPlay)
            st.button('Next', on_click=getnextvidname)

with tab2:
    history = get_history(cur_userid)

    if history:
        col1, col2 = st.columns([0.8,0.2])
        with col1:
            name = [x[2] for x in history]    
            dt = [x[3] for x in history]

            df = pd.DataFrame({'Name':name, 'Date & time':dt})
            
            df.index = np.arange(1, len(df)+1)
            st.write(df.to_html(escape=False, index=False), unsafe_allow_html=True)

        with col2:
            st.write('Delete')
            for x in range(len(history)):
                st.button('Delete', key=x, on_click=deletehistory, args=(history[x][0],))
        