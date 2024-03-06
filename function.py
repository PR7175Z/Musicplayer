import streamlit as st
import streamlit.components.v1 as components
from streamlit.components.v1 import html
import base64

#show header logo and title
def header():
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
		
#to load gif
def gifload(path):
    file_ = open(path, "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    return data_url