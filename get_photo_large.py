from bs4 import BeautifulSoup
import requests
import time
import os
from pathlib import Path

def get_html(url):
	r = requests.get(url)
	return r.text

def get_page_data(html):
	soup = BeautifulSoup(html, 'lxml')
	
	users = soup.find('div', class_='portlet_h_name_t')
	print(users)
	
	
def main():
	# устанавливаем связь
	session  = requests.Session()
	data = {'httpsdata':'Cx7eSfDS-P3vq1h0l-O_KZjIpVGJ7pgUnhQz2MMBPejVF30Mtx2nOv07jSdSS1d4EFnPYa8bZkQ6ibFbg0OEigF1EeUxgatxrI4BD7RHH3jwGQuxrwqj5lDEdhbNJmcCJjIt5UXA6du-ZXOjQTVY0njvhKkwMRmalCy8-hr3wXCOrhdYN2kuJVfHIvNBfgw7x2iGVM-Ucqzo5-KfJC4FVyfWkz7UuTxPGJQGuvV60PO6oTqcdx0F4PiwvrK_9j2C', 'field_email':'380500182297','field_password':'xvt192nv2r'}
	cookies = {'bci': '9049596122882198167', '_statid': '0c73fcaf-cb72-495c-958d-f710a7a91041', 'viewport': '1020', 'AUTHCODE': '3NVtt_J98HDbfCflHLqGZdlL2-akg-LVlpcVMcJyC_S5JceEvDWMKh7iy46799Nho844AcGkK98A8kyhM4SXg3Y9Z1fik8EmwpeKUqAaFk03e8A2TqETZQKbHzw1ncs4PXe6o_nTldpkiHw_3'}
	rs = session.post('https://ok.ru/dk?cmd=AnonymLogin&st.cmd=anonymLogin', data = data, cookies = cookies)
	
	# генерируем урл
	base_url = 'https://ok.ru/profile/568320423511/pphotos/834689400151'
	
	f = open('photos.txt')
	s = open('photos_large.txt', 'a')
	z = 0
	
	for line in f:
		rse = session.get(line.rstrip('\n'))
		soup = BeautifulSoup(rse.text, 'lxml')
		pics = soup.find('img', class_='photo-layer_img rotate__0deg')
		print(pics['src'])
		s.write('http:' + pics['src'] + '\n')
		
		z = z + 1;
		
		x = line.split("/")
		print(x[4])
		if (len(x) == 6):
			Path("D://Work/Photos/New/Female/" + x[3]).mkdir(parents=True, exist_ok=True)
			img_data = requests.get('http:' + pics['src']).content
			#os.mkdir('D://' + x[4])
			with open('D://Work/Photos/New/Female/' + x[3] + '/' + x[5].rstrip('\n') + '.jpg', 'wb') as handler:
				handler.write(img_data)
		else:
			Path("D://Work/Photos/New/Female/" + x[4]).mkdir(parents=True, exist_ok=True)
			img_data = requests.get('http:' + pics['src']).content
			#os.mkdir('D://' + x[4])
			with open('D://Work/Photos/New/Female/' + x[4] + '/' + x[6].rstrip('\n') + '.jpg', 'wb') as handler:
				handler.write(img_data)		
		
	#html = get_html(url_gen)
	#get_page_data(html)
	
	
if __name__ == '__main__':
	main()
	
	