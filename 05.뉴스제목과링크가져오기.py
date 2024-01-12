import requests
from bs4 import BeautifulSoup


response=requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90")
html = response.text
soup = BeautifulSoup(html,'html.parser')
links=soup.select(".news_tit")
for i in links:
    print(i.text)