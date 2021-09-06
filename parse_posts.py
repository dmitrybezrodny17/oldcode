from selenium import webdriver
from time import sleep 
import time
from selenium.webdriver.chrome.options import Options  
from webdriver_manager.chrome import ChromeDriverManager 
import webdriver_manager.chrome
import csv
import random
import os
import pyautogui
import pandas


class Facebook:
	def __init__(self, profile): # инициируем браузер
		self.profile_number = profile # считываем переданное значения номера профиля
		options = webdriver.ChromeOptions()
		## эмуляция мобильного
		#mobopt = mobile_emulation = {
		#	"deviceName": "Nexus 5"}
		#options.add_experimental_option("mobileEmulation", mobopt)
		## 
		options.add_argument('user-data-dir=D:\Work\Profiles\profile' + str(self.profile_number)) # передаем данные о папке профиля в опции браузера
		options.add_experimental_option("excludeSwitches", ['enable-automation']) # якобы маскируем автоматизацию
		self.driver = webdriver.Chrome(executable_path=r'chromedriver.exe', chrome_options=options) # запускаем браузер с опциями

	def nothing(self): # просто проверка
		self.driver.get('http://google.com/')
		input('Press Enter to exit')
		self.driver.close()
		
	def random_repost(self): # делаем рандом репост из .txt
		self.driver.get('http://facebook.com/') # открываем фейсбук
		posts = open('D:/Work/posts.txt', 'r') # открываем список постов
		m=posts.readlines() #
		l=[] #
		for i in range(0,len(m)-1): # считываем рандом строку
			x=m[i] #
			z=len(x) #
			a=x[:z-1] #
			l.append(a) #
		l.append(m[i+1]) #
		random_url=random.choice(l) #
		posts.close() # закрываем список постов
		self.driver.get(random_url) # переходим по ссылке поста
		time.sleep(2) # ждем прогрузку
		repost_buttons = self.driver.find_elements_by_xpath('//a[contains(@class, " _2nj7  _18vj _18vk")]') # ищем все кнопки репоста
		repost_button = repost_buttons[-1] # выбираем нужную
		repost_button.click() # нажимаем на неё
		time.sleep(3) # ждем прогрузку окна с репостом
		select_repost = self.driver.find_element_by_xpath('//a[contains(@class, "_42ft _4jy0 _55pi _5vto _55_p _2agf _4o_4 _401v _p _4jy3 _517h _51sy")]') # ищем меню выбора репоста
		select_repost.click() # нажимаем на него
		time.sleep(1) # ждем пока откроется
		select_repost_all = self.driver.find_element_by_xpath('//li[contains(@class, "_54ni _4h7j _k_c _4pmk _54nd __MenuItem")]') # ищем вариант репоста видимого всем
		select_repost_all.click() # нажимаем на него
		repost_button_last = self.driver.find_element_by_xpath('//button[contains(@class, "_2g61 _4jy0 _4jy3 _4jy1 _51sy selected _42ft")]') # ищем последнюю кнопку репоста
		repost_button_last.click() # нажимаем на него
		time.sleep(1) # ждем пока пропадет надпись о том что сделан репост
		#time.sleep(3)
		#ebuchaya_huynya = self.driver.find_element_by_xpath('//i[contains(@class, "img sp_53ttqOzw4pc sx_b466b7")]') # ну здесь можно закрыть окно с постом (фото), но не всегда работает
		#ebuchaya_huynya.click()
		
	def googleit(self, last_photo): # для теста
		self.driver.get('https://lmgtfy.com/?q=' + str(self.profile_number))
		self.profile_last_photo = last_photo
		print(self.profile_number)
		print(self.profile_last_photo)
		time.sleep(3)
		#input('Press Enter to exit')
		self.driver.close()
	

def main():
	#start_profile = input("Enter Profile Number to Start: ")
	col_list=['profile','pass','last_photo'] # обозначаем колонки в csv
	df = pandas.read_csv('acc.txt', usecols=col_list, sep=',') # открываем csv
	for index, row in df.iterrows():
		profile = int(df["profile"][index]) # даем каждому profile свой номер из первой колонки
		last_photo = int(df["last_photo"][index])
		
		bot = Facebook(profile) # передаем параметр profile
		bot.googleit(last_photo)
		df.at[index, 'last_photo'] = int(df["last_photo"][index] + 1) # меняем номер последнего загруженного фото
		df.to_csv('acc.txt', index=False) # сохраняем csv
	

if __name__ == '__main__':
	main()
	
	
	
	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	