from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import requests
import re
import pandas
import csv
import base64 
import json
import time
import pyautogui
from selenium.common.exceptions import WebDriverException
import sys
import random
import os
import pyautogui
import win32gui
import win32con
import win32api


class Facebook:
	def __init__(self, uid, profile, last_photo, url, login, password): # инициируем браузер
		#запуск браузера
		self.mla_profile_id = uid
		self.profile_name = profile
		self.last_photo = last_photo
		self.url = url
		self.login = login
		self.password = password
		mla_url = 'http://127.0.0.1:35000/api/v1/profile/start?automation=true&profileId='+self.mla_profile_id
		resp = requests.get(mla_url)
		json = resp.json()
		opt = webdriver.ChromeOptions()
		opt.add_experimental_option('w3c', False)
		opt.add_argument("--disable-notifications");
		self.driver = webdriver.Remote(command_executor=json['value'], options=opt)
		
	def ip_change(self):
		proxy_change = requests.get('http://185.70.109.21/x61x13j47ny269m1n3z3sky0r8fu4d83.php')
		if (proxy_change.status_code == 200):
			print(">> IP change OK")
			time.sleep(3)
		else:
			print(">> IP change BAD")
			self.driver.close()
			sys.exit()

	def random_repost(self): 
		posts = open('C://Users//User//Desktop//ml scripts//posts.txt', 'r') # открываем список постов
		m=posts.readlines() 
		l=[] 
		for i in range(0,len(m)-1):
			x=m[i] 
			z=len(x) 
			a=x[:z-1] 
			l.append(a) 
		l.append(m[i+1]) 
		random_url=random.choice(l) 
		posts.close() 
		self.driver.get(random_url)
		time.sleep(5) 
		try:
			self.driver.find_element_by_xpath('//span[contains(text(), "интерфейсом")]')
			print(">> DESIGN ERROR")
			return
		except WebDriverException:
			pass
		if (self.driver.find_elements_by_xpath("//div[contains(@class, 'menu_login_container rfloat _ohf')]")):
			username_box = self.driver.find_element_by_id('email')
			username_box.send_keys(self.login)
			time.sleep(1) 
			password_box = self.driver.find_element_by_id('pass') 
			password_box.send_keys(self.password) 
			login_box = self.driver.find_element_by_id('loginbutton') 
			login_box.click()  
		else:
			pass
		if (self.driver.find_elements_by_xpath("//*[contains(text(), 'К сожалению, этот контент сейчас недоступен')]")):
			print(">> Post BAD")
			random_repost()
		else:
			repost_buttons = self.driver.find_elements_by_xpath('//a[contains(@class, " _2nj7  _18vj _18vk")]') # ищем все кнопки репоста
			repost_button = repost_buttons[-1] # выбираем нужную
			try: 
				repost_button.click() # нажимаем на неё
			except WebDriverException:
				webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
				time.sleep(1)
				repost_button.click()
			time.sleep(5) # ждем прогрузку окна с репостом
			repost_button_last = self.driver.find_element_by_xpath('//button[contains(@class, "_2g61 _4jy0 _4jy3 _4jy1 _51sy selected _42ft")]') # ищем последнюю кнопку репоста
			repost_button_last.click() # нажимаем на него
			print(">> Repost OK")
			time.sleep(5) # ждем пока пропадет надпись о том что сделан репост
		
	def add_photo(self): # загрузка фото
		self.driver.get('http://facebook.com/') # открываем фейсбук
		time.sleep(5)
		
		#design
		try:
			self.driver.find_element_by_xpath('//span[contains(text(), "интерфейсом")]')
			print(">> DESIGN ERROR")
			return
		except WebDriverException:
			pass
		# 
		
		
		# login
		try:
			self.driver.find_element_by_xpath("//div[contains(@class, 'menu_login_container rfloat _ohf')]")
			username_box = self.driver.find_element_by_id('email')
			username_box.send_keys(self.login)
			time.sleep(1) 
			password_box = self.driver.find_element_by_id('pass') 
			password_box.send_keys(self.password) 
			login_box = self.driver.find_element_by_id('loginbutton') 
			login_box.click()  
		except WebDriverException:
			pass
		try:
			self.driver.find_element_by_xpath("//form[contains(@class, '_featuredLogin__formContainer')]")
			username_box = self.driver.find_element_by_id('email')
			username_box.send_keys(self.login)
			time.sleep(1) 
			password_box = self.driver.find_element_by_id('pass') 
			password_box.send_keys(self.password) 
			login_box = self.driver.find_element_by_id('royal_login_button') 
			login_box.click()  
		except WebDriverException:
			pass
		#	
			
		try:
			element = WebDriverWait(self.driver, 15).until(
				EC.presence_of_element_located((By.CLASS_NAME, "_3ixn"))
			)
			webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()	
			element.click()
		except WebDriverException:
			pass
			
		if (self.last_photo > 8):
			return
		else:
			pass
			
		self.last_photo += 1
		image_upload_button = self.driver.find_elements_by_xpath('//div[contains(@class, "_3jk")]') # ищем все кнопки загрузки фото
		image_upload_button[0].click() # нажимаем на первую
		time.sleep(5) # ждем пока откроется окно загрузки
		pyautogui.write('D:\\Work\\Photos\\New\\' + str(self.profile_name) + '\\' + str(self.last_photo) + '.jpg') # вписываем адрес нашего фото
		pyautogui.press('enter') # нажимаем энтер
		time.sleep(7) # ждем пока фото загрузится
		if (self.last_photo == 1):
			time.sleep(3)
			select_image_post = self.driver.find_element_by_xpath('//div[contains(@class, "_6a _43_1")]') # ищем меню выбора поста
			select_image_post.click() # нажимаем на него
			time.sleep(3) # ждем прогрузку
			try:
				select_image_post_all = self.driver.find_element_by_xpath('//li[contains(@class, "_54ni _4h7j _k_c _4pmk __MenuItem")]') # ищем вариант поста видимого всем
			except WebDriverException: 
				select_image_post_all = self.driver.find_element_by_xpath('//li[contains(@class, "_54ni _4h7j _k_c _4pmm __MenuItem")]') # ищем вариант поста видимого всем
			select_image_post_all.click() # нажимаем на него
		else:
			pass
		time.sleep(7) # ждем еще немножко
		try:
			repost_button_last = self.driver.find_element_by_xpath('//div[contains(@class, "_45wg _69yt")]') # ищем кнопку размещения поста
		except WebDriverException: 
			repost_button_last = self.driver.find_element_by_xpath('//span[contains(text(), "Отправить")]') # ищем кнопку размещения поста
		repost_button_last.click() # нажимаем на 
		time.sleep(7) # ждем на всякий случай
		print(">> Photo OK")
	
		#input('Press Enter to exit')
		#self.driver.close()
		
	def add_avatar(self):
		self.driver.get(self.url)
		time.sleep(3)
		if (self.driver.find_elements_by_xpath("//div[contains(@class, 'menu_login_container rfloat _ohf')]")):
			username_box = self.driver.find_element_by_id('email')
			username_box.send_keys(self.login)
			time.sleep(1) 
			password_box = self.driver.find_element_by_id('pass') 
			password_box.send_keys(self.password) 
			login_box = self.driver.find_element_by_id('loginbutton') 
			login_box.click()  
		else:
			pass
		webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
		try:
			change_ava = self.driver.find_element_by_xpath('//div[contains(@class, "s45kfl79 emlxlaya bkmhp75w spb7xbtv pmk7jnqg kavbgo14")]') # ищем кнопку смены фото
			change_ava.click()
			time.sleep(3) # ждем пока откроется окно загрузки
			avatar_upload = self.driver.find_element_by_xpath('//div[contains(@class, "buofh1pr j83agx80 oi9244e8")]') # ищем все кнопки загрузки фото
			avatar_upload.click()
			time.sleep(3) # ждем пока откроется окно загрузки
			pyautogui.write('D:\\Work\\Photos\\New\\' + str(self.profile_name) + '\\0.jpg') # вписываем адрес нашего фото
			pyautogui.press('enter') # нажимаем энтер
			time.sleep(7) 
			final_upload = self.driver.find_element_by_xpath('//span[contains(@class, "oi732d6d ik7dh3pa d2edcug0 qv66sw1b c1et5uql a8c37x1j muag1w35 enqfppq2 jq4qci2q a3bd9o3v lrazzd5p bwm1u5wc ni8dbmo4 stjgntxs ltmttdrg g0qnabr5")]') # ищем все кнопки загрузки фото
			final_upload.click()
			
		except WebDriverException: 
			change_ava = self.driver.find_element_by_xpath('//div[contains(@class, "fbTimelineProfilePicSelector")]') # ищем кнопку смены фото
			change_ava.click()
			time.sleep(3) # ждем пока откроется окно загрузки
			avatar_upload = self.driver.find_elements_by_xpath('//div[contains(@class, "_5uaq _3es7 _3es8 _4p2a")]') # ищем все кнопки загрузки фото
			avatar_upload[0].click()
			time.sleep(3) # ждем пока откроется окно загрузки
			pyautogui.write('D:\\Work\\Photos\\New\\' + str(self.profile_name) + '\\0.jpg') # вписываем адрес нашего фото
			pyautogui.press('enter') # нажимаем энтер
			time.sleep(10) 
			final_upload = self.driver.find_elements_by_xpath('//button[contains(@class, "_4jy0 _4jy3 _4jy1 _51sy selected _42ft")]') # ищем все кнопки загрузки фото
			final_upload[-1].click()
			
		time.sleep(7)
		
		
	def nothing(self):
		self.driver.get('https://google.com/')
		
	def close_browser(self):
		self.driver.close()
	

def main():
	start = input("Where to start (ie 'profile_1001'): ")
	col_list=['uid_desktop','uid_mobile','profile','login','password','first_name','second_name','url','sex','name_changed','lang','ava','last_photo','banned','cookies'] # обозначаем колонки в csv
	df = pandas.read_csv('acc100.csv', encoding='utf8', usecols=col_list, sep=',')
	for index, row in df[df['profile'] >= start].iterrows():
		uid = str(df["uid_desktop"][index])
		profile = str(df["profile"][index])
		last_photo = int(df["last_photo"][index])
		url = str(df["url"][index])
		ava = int(df["ava"][index])
		login = str(df["login"][index])
		password = str(df["password"][index])
		bot = Facebook(uid, profile, last_photo, url, login, password)
		
		print('Current profile: ' + profile)
		
		bot.nothing()
		
		# паунс в окно
		toplist = []
		winlist = []
		def enum_callback(hwnd, results):
			winlist.append((hwnd, win32gui.GetWindowText(hwnd)))
		win32gui.EnumWindows(enum_callback, toplist)
		mimic = [(hwnd, title) for hwnd, title in winlist if 'mimic' in title.lower()]
		mimic = mimic[0]
		win32gui.SetForegroundWindow(mimic[0])
		# / паунс в окно
			
		bot.ip_change()
		
		res = requests.get(str(url))
		if ('знайдена' in res.text):
			print(">> Profile BAD")
			df.at[index, 'banned'] = 1
			bot.close_browser()
		else:
			print(">> Profile GOOD")
			if (ava == 0):
				bot.add_avatar()
				print(">> Avatar OK")
				df.at[index, 'ava'] = 1
			else:
				pass
			if (last_photo < 8):
				bot.add_photo()
				last_photo += 1
				bot.random_repost()
				bot.add_photo()
				last_photo += 1
				bot.random_repost()
				bot.add_photo()
				last_photo += 1
				bot.random_repost()
			else:
				pass
			bot.close_browser()
			
			df.at[index, 'last_photo'] = last_photo
		df.to_csv('acc100.csv', index=False) # сохраняем csv
	
	

if __name__ == '__main__':
	main()
	
	
	
	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
