from selenium import webdriver 
from time import sleep 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.options import Options  
import time
import sys
from selenium.webdriver.common.keys import Keys

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

queries = open('queries.txt', 'r', encoding="utf-8")

for line in queries:
	first_url = 'https://www.facebook.com/search/pages/?q='
	last_url = '&epa=SERP_TAB'
	driver.get(first_url + line + last_url)

	new_height = 1
	while (new_height < 1000):
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		sleep(2)
		last_height = driver.execute_script("return document.body.scrollHeight")
		SCROLL_PAUSE_TIME = 2
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(SCROLL_PAUSE_TIME)
		new_height = driver.execute_script("return document.body.scrollHeight")
		last_height = new_height
		
	urls = driver.find_elements_by_xpath('//a[contains(@class, "_32mo")]')
	links = [url.get_attribute('href') for url in urls]
	for x in range(len(links)):
		print(x)
		f = open('result_pages.txt', 'a', encoding="utf-8")
		f.write(str(links[x]) + '\n')

		
		
		
		
		
		
		
		
		
		
		
		
	