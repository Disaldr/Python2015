import re
import requests
from bs4 import BeautifulSoup

text = input("Введите запрос: ")
region = int(input("Введите код региона: "))
payload = {'text': text, 'lr': region}
result = requests.get("https://yandex.ru/search/", params=payload).text
# print(resolt)

soup = BeautifulSoup(result, 'html.parser')
# print(soup.prettify())

referals = open("referals.txt", 'w')

for link in soup.find_all('a', href=re.compile('^https\:\/\/www\.')):
    referals.write(link.get('href')+'\n')

referals.close()