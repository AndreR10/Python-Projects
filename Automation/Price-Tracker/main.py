from bs4 import BeautifulSoup
from requests_html import HTMLSession
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
url = 'https://www.worten.pt/gaming/playstation/acessorios/ps4/comando-ps4-dualshock-black-v2-wireless-5962905'

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup)
