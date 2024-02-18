from time import sleep 
from selenium import webdriver 
from selenium.webdriver.firefox.service import Service 
from localStoragePy import localStoragePy 

ls = localStoragePy("db", "json") 

options = webdriver.FirefoxOptions() 
user_agent = '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'
options.add_argument(user_agent) 
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

options.add_argument("--headless") 
options.add_argument("--log-level") 
options.add_argument('--disable-application-cache') 
ser = Service("D:\\pythonlectures\\semprojectraw\\Include\\geckodriver.exe") 
driver = webdriver.Firefox(service=ser, options=options) 
extension1 = "C://Users//user//Downloads//ublock_origin-1.55.0.xpi"
driver.install_addon(extension1, temporary=True) 

def stream(MusicName): 
	driver.get(f"https://www.youtube.com/results?search_query={MusicName}") 
	driver.implicitly_wait(0.5) 
	video = driver.find_element( 
		"xpath", "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string") 
	video.click() 


def pauseAndPlay(): 
	pauseVideo = driver.find_element( 
		"xpath", "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[1]/video") 
	driver.implicitly_wait(1) 
	pauseVideo.click() 

def track(): 
	track = driver.find_element( 
		"xpath", "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[1]/h1/yt-formatted-string") 
	artist = driver.find_element( 
		"xpath", "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[1]/ytd-video-owner-renderer/div[1]/ytd-channel-name/div/div/yt-formatted-string/a") 
	print(f"{track.text} - {artist.text}") 


def streamPlaylist(playlistName): 
	url = ls.getItem(playlistName) 

	if url != None: 
		driver.get(url) 
		driver.implicitly_wait(2.5) 
		shuffle = driver.find_element( 
			"xpath", "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-playlist-header-renderer/div/div[2]/div[1]/div/div[2]/ytd-button-renderer[2]/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]") 
		shuffle.click() 
	else: 
		print("playlist not found......") 
		print("re enter name properly") 


def addPlaylist(name, url): 
	ls.setItem(name, url) 
	sleep(1) 
	print("stored....") 


def removePlaylist(playlistName): 
	ls.removeItem(playlistName) 
	print("removed....") 


def stop(): 
	driver.quit() 
	exit(1) 


# we need to use Stream {songname} for our player to stream the song 
if __name__ == "__main__": 
	print("Enter the name of song") 
	while True: 
		uinput = str(input()) 
		# splitting the uinput in 2 strings and access the first string 
		if uinput.split(" ", 1)[0] == "st": 
			songName = uinput.split(" ", 1)[1] 
			print(songName)
			stream(songName) 

		# elif uinput == "track": 
		# 	track() 

		# 	# elif uinput == 'add': 
		# 	# url = str(input("enter url of playlist")) 
		# 	# Name = str(input("enter name of playlist:")) 
		# 	# addPlaylist(Name, url) 

		# elif uinput.split(" ", 1)[0] == "pt": 
		# 	pName = uinput.split(" ", 1)[1] 
		# 	streamPlaylist(pName) 

		# elif uinput.split(" ", 1)[0] == "rem": 
		# 	name = uinput.split(" ", 1)[1] 
		# 	removePlaylist(name) 

		elif uinput == "stop": 
			stop() 

		else: 
			print("invalid command") 
