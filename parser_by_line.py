from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
import pandas
import csv
from selenium.webdriver.chrome.options import Options

class Parsers:
	def __init__(self):
		chrome_options = Options()
		chrome_options.add_argument("--headless")
		self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options) 
		
	def default(self):
		with open('urls.txt') as q:
			urls = q.readlines()
		for url in urls:
			self.driver.get(url)
			''' проверка на страницу товара ''' 
			if not (self.driver.find_elements_by_class_name("j-tabs")):
				continue
			''' название товара '''
			title = self.driver.find_element_by_xpath("/html/body/main/article/div[2]/div[2]/h1")
			''' цена товра ''' 
			price = self.driver.find_element_by_xpath("/html/body/main/article/div[2]/div[2]/div[3]/div/div/div/span")
			''' кол-во товара '''
			try:
				sht = self.driver.find_element_by_xpath("//*[contains(text(), 'Кол-во в уп., шт.')]/following-sibling::span/following-sibling::span")
				quantity = sht.get_attribute('innerText')
			except Exception:
				quantity = '1'
			''' объявляем таблицу и вписываем '''
			col_list=['name', 'price', 'quantity', 'url'] 
			df = pandas.read_csv('.csv', encoding='utf8', usecols=col_list, sep=',')	
			df.at[url, 'url'] = url
			df.at[url, 'name'] = title.get_attribute('innerText')
			df.at[url, 'quantity'] = quantity	
			df.at[url, 'price'] = price.get_attribute('innerText').replace(',', '.').replace(' ', '')
			df.to_csv('.csv', index=False)

	def coffee2go(self):
		with open('urls.txt') as q:
			urls = q.readlines()
		for url in urls:
			self.driver.get(url)
			if not (self.driver.find_elements_by_class_name("j-tabs")):
				continue
			title = self.driver.find_element_by_xpath("/html/body/main/article/div[2]/div[2]/h1")
			price = self.driver.find_element_by_xpath("/html/body/main/article/div[2]/div[2]/div[3]/div/div/div/span")
			try:
				sht = self.driver.find_element_by_xpath("//*[contains(text(), 'Кол-во в уп., шт.')]/following-sibling::span/following-sibling::span")
				quantity = sht.get_attribute('innerText')
			except Exception:
				quantity = '1'
			col_list=['name', 'price', 'quantity', 'url'] 
			df = pandas.read_csv('coffee2go.csv', encoding='utf8', usecols=col_list, sep=',')	
			df.at[url, 'url'] = url
			df.at[url, 'name'] = title.get_attribute('innerText')
			df.at[url, 'price'] = price.get_attribute('innerText').replace(',', '.').replace(' ', '')
			df.at[url, 'quantity'] = quantity
			df.to_csv('coffee2go.csv', index=False)
			
	def impack_com_ua(self):
		with open('urls.txt') as q:
			urls = q.readlines()
		for url in urls:
			self.driver.get(url)
			if not (self.driver.find_elements_by_class_name("b-product-info")):
				continue
			title = self.driver.find_element_by_xpath('//h1[contains(@class, "b-caption b-online-edit")]')
			price = self.driver.find_element_by_xpath('//p[contains(@class, "b-product-cost__price")]')
			try:
				sht = self.driver.find_element_by_xpath("//*[contains(text(), 'Количество в упаковке')]/following-sibling::td")
				quantity = sht.get_attribute('innerText')
			except Exception:
				quantity = '1'
			col_list=['name', 'price', 'quantity', 'url'] 
			df = pandas.read_csv('impack_com_ua.csv', encoding='utf8', usecols=col_list, sep=',')	
			df.at[url, 'url'] = url
			df.at[url, 'name'] = title.get_attribute('innerText')
			df.at[url, 'price'] = price.get_attribute('innerText').replace(',', '.').replace(' ', '')
			df.at[url, 'quantity'] = quantity.replace('(', '').replace(')', '').replace('.', '').replace('шт', '').replace(' ', '')
			df.to_csv('impack_com_ua.csv', index=False)
			
	def petrovka_horeca_com_ua(self):
		with open('urls.txt') as q:
			urls = q.readlines()
		for url in urls:
			self.driver.get(url)
			if not (self.driver.find_elements_by_class_name("b-product-info")):
				continue
			title = self.driver.find_element_by_xpath('//h1[contains(@class, "b-product__name b-title b-online-edit")]')
			if (self.driver.find_element_by_xpath('//p[contains(@class, "b-product-cost__unknown-price")]')):
				break
			price = self.driver.find_element_by_xpath('//p[contains(@class, "b-product-cost__price")]')
			try:
				sht = self.driver.find_element_by_xpath("//*[contains(text(), 'Количество в упаковке')]/following-sibling::td")
				quantity = sht.get_attribute('innerText')
			except Exception:
				quantity = '1'
			col_list=['name', 'price', 'quantity', 'url'] 
			df = pandas.read_csv('petrovka_horeca_com_ua.csv', encoding='utf8', usecols=col_list, sep=',')	
			df.at[url, 'url'] = url
			df.at[url, 'name'] = title.get_attribute('innerText')
			df.at[url, 'price'] = price.get_attribute('innerText').replace(',', '.').replace(' ', '')
			df.at[url, 'quantity'] = quantity.replace('(', '').replace(')', '').replace('.', '').replace('шт', '').replace(' ', '')
			df.to_csv('petrovka_horeca_com_ua.csv', index=False)
			print("--- %s seconds ---" % (time.time() - start_time))
			

		
	def quit(self):
		self.driver.quit()
			
def main():
	shop = input("Enter shop name: ")
	parser = Parsers()
	if (shop == 'coffee2go'):
		parser.coffee2go()
	elif (shop == 'impack'):
		parser.impack_com_ua()
	elif (shop == 'petrovka'):
		parser.petrovka_horeca_com_ua()
	parser.quit()
		
if __name__ == '__main__':
	main()
	