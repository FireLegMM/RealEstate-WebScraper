import requests
from bs4 import BeautifulSoup as bs
import json

url = 'https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/powiat-wolominski?distanceRadius=0&locations=%5Bsubregions-200%5D&viewType=listing'

data = requests.get(url)


soup = bs(data.content,'html.parser')


soup_list = soup.find(type="application/ld+json")

data = json.loads(soup_list.text)

print(data)




