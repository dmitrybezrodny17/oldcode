from selenium import webdriver 
from time import sleep 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.options import Options  
import time
import sys

#auth
driver = webdriver.Chrome(ChromeDriverManager().install()) 
driver.get('https://www.facebook.com/') 
print ("Opened facebook") 
sleep(1) 
username_box = driver.find_element_by_id('email') 
username_box.send_keys('380500182297') 
print ("Email Id entered") 
sleep(1) 
password_box = driver.find_element_by_id('pass') 
password_box.send_keys('Xvt!92nv2rxvt192nv2r') 
print ("Password entered") 
login_box = driver.find_element_by_id('loginbutton') 
login_box.click() 
print ("Logged in") 
sleep(1)

pages = open('pages.txt', 'r', encoding="utf-8")

for line in pages:
	driver.get(line)
	print("Opened page " + line)
	new_height = 1
	while (new_height < 10000):
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		sleep(2)
		last_height = driver.execute_script("return document.body.scrollHeight")
		SCROLL_PAUSE_TIME = 2
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(SCROLL_PAUSE_TIME)
		new_height = driver.execute_script("return document.body.scrollHeight")
		#if new_height == last_height:
		#   break
		last_height = new_height
		
		posts = driver.find_elements_by_xpath('//a[contains(@class, "_5pcq")]')
		allposts = len(posts)
		print (allposts)
	links = [post.get_attribute('href') for post in posts]
	for x in range(len(links)):
		cut = str(links[x]).split("/")
		if (len(cut) > 6):
			#print(cut[0],cut[1],cut[2],cut[3],cut[4],cut[5],cut[6], sep="/")
			f = open('result_posts.txt', 'a')
			f.write(links[x].rsplit('/', 1)[0] + '\n')
		else:
			pass
	new_height = 1

	

print("Finished") 
sys.exit()





















