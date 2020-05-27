import requests
from bs4 import BeautifulSoup
import re
import os
import urllib

path = os.getcwd()
print(path)
URL = input("Введите адрес сайта: ")
folder = input("Введите название папки: ")
while True:
    try:
        os.mkdir(folder)
    except:
        print("Такая папка уже существует")
        folder = input("Введите другое название")
    else:
        break
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all('img', src = re.compile('\/[a-z\-\d\/]+.jpg'))
print(results)


arr=[]
for i in range(0, len(results)):
    arr.append(results[i]['src'])

    img_data = requests.get("https://www.combook.ru"+arr[i]).content
    handler = open(folder+"/"+str(i)+'.jpg', 'wb')
    handler.write(img_data)
    handler.close()




# site = open("index.html", encoding='utf-8')
# content = site.read()
# soup = BeautifulSoup(content, 'html.parser')
# print(soup.title.string)
# print(soup.find_all('p'))