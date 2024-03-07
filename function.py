import streamlit as st
import streamlit.components.v1 as components
from streamlit.components.v1 import html
from pathlib import Path
import base64

#show header logo and title
def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded
def img_to_html(img_path, classname):
    img_html = "<img src='data:image/png;base64,{}' class='{}'>".format(
      img_to_bytes(img_path),
      classname
    )
    return img_html

def header():
	logo = 'assets/images/logo.png'
	st.markdown(
		'''
		<style>
			button[title="View fullscreen"]{
				visibility: hidden;
			}
            .logoimage{
				width:40px;
			}
			.gifimg{
				width: 500px;
			}
		</style>
		''',unsafe_allow_html=True
	)
	row1col1, row1col2 = st.columns([0.1, 0.9])
	with row1col1:
		# logo = '/assets/images/logo.png'
		# st.markdown(f'<img src="{logo}" class="logoimage">', unsafe_allow_html=True)
		st.markdown(img_to_html(logo, classname='logoimage'), unsafe_allow_html=True)
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