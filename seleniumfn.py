from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service 
import streamlit as st
import time
from datetime import datetime
from function import *

options = webdriver.FirefoxOptions() 
user_agent = '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'
options.add_argument(user_agent) 
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

options.add_argument("--headless") 
options.add_argument("--log-level") 
options.add_argument('--disable-application-cache') 
driver = webdriver.Firefox(options=options) 

extension1 = "D://pythonlectures//semprojectraw//include//ublock_origin-1.55.0.xpi"
driver.install_addon(extension1, temporary=True) 

def stream(MusicName, driver=driver):
	try:
		driver.get(f"https://www.youtube.com/results?search_query={MusicName}") 
		driver.implicitly_wait(0.5)
		video = driver.find_element( 
			"xpath", "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string") 
		video.click()
		cur_userid = st.session_state.logged_in_id
		date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		name = get_name()
		st.write(f'Now playing: {name}')
		st.write(f'Artist: {get_channel_name()}')
		st.write(f'Views: {get_views()}')
		st.write(f'Published: {get_date()}')
		# st.markdown(f'<img src="data:image/gif;base64,{data_url}" class="gifimg" alt="musicgif">',unsafe_allow_html=True)
		insert_history(cur_userid, name, date_time)
		st.button('Stop', on_click=pauseAndPlay)
		st.button('Next', on_click=getnextvidname)
	except:
		st.error("No internet Connection")

def pauseAndPlay(driver=driver): 
    pauseVideo = driver.find_element( 
        "xpath", "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[1]/video") 
    driver.implicitly_wait(1) 
    pauseVideo.click() 

def getnextvideolink(driver=driver):
	nextvid_link = driver.find_element(
		"xpath", "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[2]/div/div[4]/ytd-watch-next-secondary-results-renderer/div[2]/ytd-compact-video-renderer[1]/div[1]/ytd-thumbnail/a")
	nextvid = driver.find_element(
		"xpath", "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[2]/div/div[4]/ytd-watch-next-secondary-results-renderer/div[2]/ytd-compact-video-renderer[1]")
	driver.implicitly_wait(1)
	print(nextvid_link)
	print(nextvid)
	# print(nextvid_link.get_attribute("href"))
 
def getnextvidname(driver=driver):
	nextvidname = driver.find_element(
		"xpath", "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[2]/div/div[4]/ytd-watch-next-secondary-results-renderer/div[2]/ytd-compact-video-renderer[1]/div[1]/div/div[1]/a/h3/span")
	driver.implicitly_wait(1)
	stream(nextvidname.text)
	print(nextvidname.text)

def get_name(driver=driver):
	vid_title = driver.find_element(
		"xpath", "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[1]/h1/yt-formatted-string")
	time.sleep(1.5)
	return vid_title.text

def get_channel_name(driver=driver):
	channel_title = driver.find_element(
		"xpath", "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[1]/ytd-video-owner-renderer/div[1]/ytd-channel-name/div/div/yt-formatted-string/a")
	return channel_title.text

def get_views(driver=driver):
	view_count = driver.find_element(
		"xpath", "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[4]/div[1]/div/ytd-watch-info-text/div/yt-formatted-string/span[1]")
	return view_count.text.split()[0]

def get_date(driver=driver):
	date = driver.find_element(
		"xpath", "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[4]/div[1]/div/ytd-watch-info-text/div/yt-formatted-string/span[3]")
	return date.text

def stop(driver=driver): 
	driver.quit() 

if __name__ == "__main__": 
	print("Enter the name of song") 
	while True: 
		try:
			uinput = str(input()) 
			if uinput.split(" ", 1)[0] == "st": 
				songName = uinput.split(" ", 1)[1] 
				print(songName)
				stream(songName)
			elif uinput == "play":
				pauseAndPlay()
			elif uinput == 'next':
				getnextvideolink()
			elif uinput == 'name':
				print(get_name())
				print(get_channel_name())
				print(get_views())
				print(get_date())
			elif uinput == "stop": 
				stop() 

			else: 
				print("invalid command") 
		except:
			stop()
