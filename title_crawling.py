import requests
from bs4 import BeautifulSoup
import pyautogui

while True:
    query=pyautogui.prompt("검색어를 입력하세요: ")
    if query =="q":
        break
    response = requests.get(f"https://search.naver.com/search.naver?where=news&query={query}")
    html = response.text
    soup = BeautifulSoup(html,'html.parser')
    titles=soup.select(".news_tit")
    for i in titles:
        print(i.text)
    print()