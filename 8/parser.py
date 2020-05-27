import requests
from bs4 import BeautifulSoup
import re
import urllib
import os


#Сегодня мы попробуем написать парсер простого сайта, такого к примеру, как https://www.combook.ru/


path_now = os.getcwd()
print(os.getcwd())
URL = "https://ria.ru/ips/asus-etiquette/"
name_folder = "ria"
try:
	os.mkdir(name_folder)
except:
	print("Бывает")
page = requests.get(URL)


count = 0

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all('img', src = re.compile('\/[a-z\-\d\/]+.png'))
print(results)
count = count+1
print(count)

our_arr = []

for i in range(0, len(results)):

	our_arr.append(results[i]['href'])
	print(results[i])
	img_data = requests.get("https://ria.ru/ips/asus-etiquette/"+our_arr[i]).content
	with open(name_folder+"/"+str(i)+".jpg", 'wb') as handler:
		handler.write(img_data)





