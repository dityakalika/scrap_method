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


# MENGAMBIL DARI SINGLE QUOTE

quote = soup.find('span', class_='text')
author = soup.find('small', class_='author')
tags = [tag.text for tag in soup.find('div', class_='tags').find_all('a', class_='tag')]

print(quote.text)
print(author.text)
print(tags)

