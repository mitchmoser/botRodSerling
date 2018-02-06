#!/usr/bin/env python3
# scrape Rod Serling monologues from Wiki
import requests
from bs4 import BeautifulSoup

url = 'https://en.wikiquote.org/wiki/The_Twilight_Zone_(1959_TV_series)#Opening_narrations'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, "html.parser")
wiki = soup.find_all('dd')

with open('rod.txt', 'w') as output:
    for quote in wiki:
        line = quote.get_text().replace('Rod Serling: ', '')
        output.write(line + "\n")
output.close()
