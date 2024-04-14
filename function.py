import streamlit as st
import streamlit.components.v1 as components
from streamlit.components.v1 import html
from pathlib import Path
import base64
import psycopg2
from config import load_config

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

#function for the header call
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
            [data-testid="stHorizontalBlock"] {
                align-items: center;
            }
		</style>
		''',unsafe_allow_html=True
	)
	row1col1, row1col2 = st.columns([0.1, 0.9])
	with row1col1:
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

#encode password
def encode_password(password):
    password_bytes = password.encode("ascii") 
    base64_password = base64.b64encode(password_bytes) 
    encoded_password = base64_password.decode("ascii") 
    return encoded_password

def decode_password(password):
    password_bytes = password.encode("ascii") 
    base64_password = base64.b64decode(password_bytes) 
    decoded_password = base64_password.decode("ascii") 
    return decoded_password

# inserting user in db
def insert_user(first_name, last_name, email, password):
    password=encode_password(password)
    sql = """INSERT INTO users(first_name,last_name, email, password)
             VALUES(%s, %s, %s, %s) RETURNING user_id;"""
    
    user_id = None
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(sql, (first_name,last_name, email, password))

                # get the generated id back                
                rows = cur.fetchone()
                if rows:
                    user_id = rows[0]

                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return user_id
    
#Retrieve data from the users table
def get_users():
    config  = load_config()
    userdata = []
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT user_id, email, password FROM users")
                # print("The number of parts: ", cur.rowcount)
                row = cur.fetchone()

                while row is not None:
                    userdata.append(row)
                    row = cur.fetchone()
                return userdata

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

#page navigation
def nav_page(page_name, timeout_secs=3):
    nav_script = """
        <script type="text/javascript">
            function attempt_nav_page(page_name, start_time, timeout_secs) {
                var links = window.parent.document.getElementsByTagName("a");
                for (var i = 0; i < links.length; i++) {
                    if (links[i].href.toLowerCase().endsWith("/" + page_name.toLowerCase())) {
                        links[i].click();
                        return;
                    }
                }
                var elasped = new Date() - start_time;
                if (elasped < timeout_secs * 1000) {
                    setTimeout(attempt_nav_page, 100, page_name, start_time, timeout_secs);
                } else {
                    alert("Unable to navigate to page '" + page_name + "' after " + timeout_secs + " second(s).");
                }
            }
            window.addEventListener("load", function() {
                attempt_nav_page("%s", new Date(), %d);
            });
        </script>
    """ % (page_name, timeout_secs)
    html(nav_script)

def hide_sidebar():
    st.markdown("""
    <style>
        section[data-testid="stSidebar"][aria-expanded="true"]{
            display: none;
        }
    </style>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    # insert_user("adam", "eve", "adameve@gmail.com", "test")
    print(get_users())
    