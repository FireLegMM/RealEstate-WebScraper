import requests
from bs4 import BeautifulSoup as bs
import json
import os
from datetime import datetime

url = 'https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/powiat-wolominski?distanceRadius=0&locations=%5Bsubregions-200%5D&viewType=listing&limit=72'
data_path = './web-scraper/data/'
data = requests.get(url)


soup = bs(data.content,'html.parser')


soup_list = soup.find(type="application/json")

data = json.loads(soup_list.text)
page_count = data['props']['pageProps']['data']['searchAds']['pagination']['totalPages']
dane = data['props']['pageProps']['data']['searchAds']['items']

for page in range(2,page_count+1):
    url = f'https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/powiat-wolominski?distanceRadius=0&locations=%5Bsubregions-200%5D&viewType=listing&limit=72&page={str(page)}'
    data = requests.get(url)
    soup = bs(data.content,'html.parser')
    soup_list = soup.find(type="application/json")
    data = json.loads(soup_list.text)
    dane_new = data['props']['pageProps']['data']['searchAds']['items']
    dane.extend(dane_new)

now = datetime.now()
date_str = now.strftime('%Y%m%d')

file_name = f'data_{date_str}.json'
with open(data_path + file_name, 'a+', encoding='utf-8') as f:
    json.dump(dane, f, ensure_ascii=False, indent=4)
