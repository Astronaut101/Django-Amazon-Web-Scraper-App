import requests
from bs4 import BeautifulSoup

# URLs
book_01_url = "https://www.amazon.com/Django-Example-powerful-reliable-applications/dp/1801813051"
book_02_url = "https://www.amazon.com/Fluent-Python-Luciano-Ramalho-ebook/dp/B09WZJMMJP/ref=sr_1_1?crid=106OP5MJHVF5V&keywords=Fluent+Python&qid=1663563128&s=digital-text&sprefix=fluent+python%2Cdigital-text%2C420&sr=1-1"
book_03_url = "https://www.amazon.com/Hacking-APIs-Application-Programming-Interfaces/dp/1718502443"

# -- =================================

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
    # print(name)

    price = soup.select_one(selector=".header-price").getText()
    price = price.strip()
    price = float(price[1:])
    # print(price)

    return name, price


print(get_link_data(book_01_url))
print(get_link_data(book_02_url))
print(get_link_data(book_03_url))