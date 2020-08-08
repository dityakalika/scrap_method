from bs4 import BeautifulSoup
import pandas as pd
import requests

# REQUESTS DATA

URL ='http://quotes.toscrape.com/'
response = requests.get(URL)

if response.status_code != 200:
    print('The website isn\'t available')
else:
    print('The website is good')

# PARSE HTML

soup = BeautifulSoup(response.text, 'html.parser')
#print(soup)


# MENGAMBIL DARI 1 HALAMAN PENUH (MULTIPLE QUOTE)

quotes = soup.find_all('div', class_='quote')

for q in quotes:

    quote = q.find('span', class_='text').text
    author = q.find('small', class_='author').text
    tags = [tag.text for tag in q.find('div', class_='tags').find_all('a', class_='tag')]

    print(quote)
    print(author)
    print(tags)
