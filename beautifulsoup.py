# HTML 분석을 위한 파이썬 라이브러리

import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.naver.com")
html = response.text
soup=BeautifulSoup(html,'html.parser')
word = soup.select_one('.logo_sports>span')
print(word)
