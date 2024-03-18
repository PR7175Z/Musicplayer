from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service 

# extension1 = "C://Users//user//Downloads//ublock_origin-1.55.0.xpi"
options = webdriver.FirefoxOptions() 
user_agent = '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'
options.add_argument(user_agent) 
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

options.add_argument("--headless") 
options.add_argument("--log-level") 
options.add_argument('--disable-application-cache') 
ser = Service("D:\\pythonlectures\\semprojectraw\\include\\geckodriver.exe") 
driver = webdriver.Firefox(service=ser, options=options) 
# driver = webdriver.Firefox(options=options) 

extension1 = "C://Users//user//Downloads//ublock_origin-1.55.0.xpi"
driver.install_addon(extension1, temporary=True) 

def stream(MusicName):
	driver.get(f"https://www.youtube.com/results?search_query={MusicName}") 
	driver.implicitly_wait(0.5) 
	print(driver.session_id == 'None')
	video = driver.find_element( 
		"xpath", "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string") 
	video.click()
	return True

def stop(): 
	driver.quit() 

# we need to use Stream {songname} for our player to stream the song 
if __name__ == "__main__": 
	print("Enter the name of song") 
	while True: 
		try:
			uinput = str(input()) 
			# splitting the uinput in 2 strings and access the first string 
			if uinput.split(" ", 1)[0] == "st": 
				songName = uinput.split(" ", 1)[1] 
				print(songName)
				stream(songName) 
			elif uinput == "stop": 
				stop() 

			else: 
				print("invalid command") 
		except:
			stop()
