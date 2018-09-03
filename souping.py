import requests
from bs4 import BeautifulSoup


def spider(max_pages):
    page = 1

    while page < max_pages:
        url = 'https://webdesignledger.com/worst-websites-ever' + str(page) + '/#068e1b0ddf'
        source_code = requests.get(url)
        plain_text = source_code.text
        #print(plain_text)
        soup = BeautifulSoup(plain_text)
        print(soup)
        for link in soup.findAll('a', {'class': 'brand'}):
            href = link.get('href')
            print(href)
            page += 1


spider(4)
