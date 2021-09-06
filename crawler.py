from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
import pandas
import csv

class Crawlers:
	def __init__(self, url):
		self.url = url
		self.driver = webdriver.Chrome(ChromeDriverManager().install()) 

	def sorter(self):
		while(True):
			col_list=['url', 'name', 'visited'] 
			df = pandas.read_csv('cr2.csv', encoding='utf8', usecols=col_list, sep=',')
			number_of_links = len(df.index)
			print("number of links" + str(number_of_links))
			position = number_of_links + 1 
			for i in range (0, number_of_links):
				number_of_links = len(df.index)
				url = str(df["url"][i])
				print(url)
				visited = int(df["visited"][i])
				if (visited == 0):
					self.driver.get(url)
					title = self.driver.title
					df.at[i, 'visited'] = 1
					df.at[i, 'name'] = str(title)
					df.to_csv('cr2.csv', index=False)
					links = self.driver.find_elements_by_xpath("//a[@href]")
					for link in links:
						href = link.get_attribute('href')
						df2 = pandas.read_csv('cr2.csv', encoding='utf8', usecols=col_list, sep=',')				
						if (df['url'].eq(str(href)).any()):
							pass
						else:
							if (("/petrovka-horeca.com.ua/" in href) and ("#" not in href) and ("cart" not in href) and ("Cart" not in href) and ("jpg" not in href) and ("png" not in href)):
								print(href)
								df.at[position, 'url'] = str(href)
								df.at[position, 'visited'] = 0
								position = position + 1
								print("position: " + str(position))
							else:
								pass
							df.to_csv('cr2.csv', index=False)
				else:
					pass	
	
def main():
	url = input("input url:...")
	crawl = Crawlers(url)
	crawl.sorter()

if __name__ == '__main__':
	main()
	
	