import requests
# import lxml
from bs4 import BeautifulSoup


def get_link_data(url):
    # Header specs
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0",
        "Accept-Language": "en",
    }

    # Start of Main Web Scraping
    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    name = soup.select_one(selector="#productTitle").getText()
    name = name.strip()

    price = soup.select_one(selector=".header-price").getText()
    price = price.strip()
    price = float(price[1:])

    return name, price