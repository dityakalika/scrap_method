from bs4 import BeautifulSoup
import pandas as pd
import requests

# MENGAMBIL DARI BEBERAPA HALAMAN (MULTIPLE PAGES)

for page in range(1,11):
    if page == 1:
        url = "http://quotes.toscrape.com"
    else:
        url = "http://quotes.toscrape.com/page/" + str(page)

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    print(url)

    quotes = soup.find_all('div', class_='quote')

    for q in quotes:
        quote = q.find('span', class_='text').text
        author = q.find('small', class_='author').text
        tags = [tag.text for tag in q.find('div', class_='tags').find_all('a', class_='tag')]

        print(quote)
        print(author)
        print(tags)