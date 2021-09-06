from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import requests
import pandas
import csv
import base64
import json
import time
import pyautogui
from selenium.common.exceptions import WebDriverException
import sys


class Facebook:
	def __init__(self, uid, profile, sex, name_changed, lang, first_name, second_name, password):
		#запуск браузера
		self.mla_profile_id = uid
		self.profile_name = profile
		self.sex = sex
		self.name_changed = name_changed
		self.lang = lang
		self.first_name = first_name
		self.second_name = second_name
		self.password = password
		mla_url = 'http://127.0.0.1:35000/api/v1/profile/start?automation=true&profileId='+self.mla_profile_id
		resp = requests.get(mla_url)
		json = resp.json()
		opt = webdriver.ChromeOptions()
		opt.add_experimental_option('w3c', False)
		opt.add_argument("--disable-notifications");
		try:
			self.driver = webdriver.Remote(command_executor=json['value'], options=opt)
		except KeyError:
			pass
	
	def ip_change(self):
		print('Current profile: ' + self.profile_name)
		proxy_change = requests.get('http://185.70.109.21/x61x13j47ny269m1n3z3sky0r8fu4d83.php')
		if (proxy_change.status_code == 200):
			print("IP change successful!")
		else:
			print("IP change unsuccessful!")
			self.driver.close()
			sys.exit()

	def language_change(self):
		if (self.lang == 0):
			try:
				time.sleep(2)
				self.driver.get('https://m.facebook.com/language.php')
				webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
				time.sleep(2)
				language = self.driver.find_element_by_xpath('//div[contains(@value, "ru_RU")]')
				self.driver.execute_script('arguments[0].click();', language)
				touch_actions = TouchActions(self.driver)
				touch_actions.tap(language)
				print("Language change successful!")
				time.sleep(2)
			except WebDriverException:
				pass
				print("Language not changed")
		else:
			pass
			print("Language not changed")
		
	def name_change(self):
		if (self.name_changed == 0):
			self.driver.get('https://m.facebook.com/settings/account/?name')
			first_name = self.driver.find_element_by_xpath('//input[contains(@name, "primary_first_name")]')
			first_name.clear()
			first_name.send_keys(self.first_name)
			last_name = self.driver.find_element_by_xpath('//input[contains(@name, "primary_last_name")]')
			last_name.clear()
			last_name.send_keys(self.second_name)
			submit_button = self.driver.find_element_by_xpath('//button[contains(@name, "save")]')
			self.driver.execute_script('arguments[0].click();', submit_button)
			time.sleep(1)
			password = self.driver.find_element_by_xpath('//input[contains(@name, "save_password")]')
			password.send_keys(self.password)
			submit2_button = self.driver.find_element_by_xpath('//button[contains(@name, "save")]')
			self.driver.execute_script('arguments[0].click();', submit2_button)
			print("Name change successful!")
			time.sleep(2)
		else:
			pass
			print("Name not changed")
		
	def sex_change(self):
		if (self.sex == 0):
			self.driver.get('https://m.facebook.com/profile/edit/infotab/section/forms/?section=basic-info')
			sexlist = self.driver.find_elements_by_xpath('//label[contains(@class, "_5aqb touchable _skt")]')
			self.driver.execute_script('arguments[0].click();', sexlist[1])
			submit_button = self.driver.find_element_by_xpath('//button[contains(@class, "_54k8 _52jg _56bs _26vk _56bu")]')
			self.driver.execute_script('arguments[0].click();', submit_button)
			print("Sex change successful!")
			time.sleep(2)
		else:
			pass
			print("Sex not changed")
		
	def nothing(self):
		self.driver.get('https://m.facebook.com/')
		
	def get_cookies(self):
		self.driver.get('https://m.facebook.com/')
		print(self.driver.get_cookies())
		
	def close_browser(self):
		self.driver.close()
		
		
def main():
	start = input("Where to start (ie 'profile_1001'): ")
	col_list=['uid_desktop','uid_mobile','profile','login','password','first_name','second_name','url','sex','name_changed','lang','ava','last_photo','banned','cookies'] # обозначаем колонки в csv
	df = pandas.read_csv('acc100.csv', encoding='utf8', usecols=col_list, sep=',')
	for index, row in df[df['profile'] >= start].iterrows():
		uid = str(df["uid_mobile"][index])
		profile = str(df["profile"][index])
		sex = df["sex"][index]
		name_changed = df["name_changed"][index]
		lang = df["lang"][index]
		first_name = str(df["first_name"][index])
		second_name = str(df["second_name"][index])
		password = str(df["password"][index])
		url = str(df["url"][index])
		
		
		bot = Facebook(uid, profile, sex, name_changed, lang, first_name, second_name, password)
		bot.ip_change()
		
		res = requests.get(str(url))
		if ('знайдена' in res.text):
			print("Profile banned!")
			df.at[index, 'banned'] = 1
			bot.close_browser()
		else:
			bot.nothing()
			'''
			bot.language_change()
			df.at[index, 'lang'] = 1
			bot.name_change()
			df.at[index, 'name_changed'] = 1
			bot.sex_change()
			df.at[index, 'sex'] = 1'''
			bot.close_browser()
		
		df.to_csv('acc100.csv', index=False) # сохраняем csv
		time.sleep(5)
		
	

if __name__ == '__main__':
	main()
	