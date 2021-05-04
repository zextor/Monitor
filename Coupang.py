import re
import requests
from bs4 import BeautifulSoup
import time

h =  { "Host": "www.coupang.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache" }

def check():
    URL = "https://www.coupang.com/np/promotion/51830/"
    res = requests.get(URL, headers=h)
    soup = BeautifulSoup(res.text, 'lxml')
    wrapper = soup.find_all('div', {'class': 'promotion-category'})
    for item in wrapper:
        name = item.find_all('span', {'class': 'category-name'})
        if name[0].text == "11Pro":
            phones = item.find_all('li')
            for phone in phones:
                link = phone.findChild()["href"]
                #https://www.coupang.com/vp/products/1637977118?itemId=1016372713&vendorItemId=5452858878
                #                       /vp/products/1637977118?itemId=1016372726&vendorItemId=5452858902
                l = "https://www.coupang.com" + link
                card = phone.find_all('span', {'class': 'ccid-txt'})
                for c in card:
                    r = re.findall(r'([0-9]+)%', c.text)
                    discount = int(r[0])
                    print(discount)
                    if discount >= 30 :
                        print(l)
    print("OK")

if __name__ == '__main__':
    while True:
        check()
        time.sleep(5)
