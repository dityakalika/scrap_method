from bs4 import BeautifulSoup
import pandas as pd
import requests

# REQUESTS DATA

url = 'https://mojok.co/'
response =requests.get(url)

if response.status_code != 200:
    print('The website isn\'t available')
else:
    print('The website is good')

# PARSE HTML

soup = BeautifulSoup(response.text, 'html.parser')
#print(soup)

terbaru = soup.find(attrs={'class':'cb-main clearfix cb-module-block'})
judul =terbaru.find_all(attrs={'class':'cb-post-title'})
penulis =terbaru.find_all(attrs={'class':'cb-author'})

for m in judul:
    print(m.text)
for x in penulis:
    print(x.text)

