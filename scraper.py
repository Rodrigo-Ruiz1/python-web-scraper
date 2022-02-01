from urllib.request import urlopen
from bs4 import BeautifulSoup

url_to_scrape = "https://fineartamerica.com/shop/posters/animal"

request_page = urlopen(url_to_scrape)
page_html = request_page.read()
request_page.close()

html_soup = BeautifulSoup(page_html, 'html.parser')

art = html_soup.find_all('div', class_="searchengineresultdiv imageProductDiv")
# print(art)

filename = 'product.csv'
f = open(filename, 'w')

headers = ' Title, Price \n '

for product in art:
    title = product.find('span', class_="imageTitle").text
    price = product.find('p', class_="productprice").text
    print(price)
    f.write(f"{title},{price}")

f.close()