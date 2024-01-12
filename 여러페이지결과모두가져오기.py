import requests
from bs4 import BeautifulSoup
import pyautogui
str='='
print("크롤링을 시작합니다.")
while True:
    query=pyautogui.prompt("검색어를 입력하세요: (종료시 q)")
    if query =="q":
        break
    else:
        num_last_page =int(pyautogui.prompt("마지막 번호를 입력해주세요: "))
        for idx,start in enumerate(range(1,num_last_page*10+1,10)):
            response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_pge&query={query}&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=310&mynews=0&office_type=0&office_section_code=0&news_office_checked=&office_category=0&service_area=0&nso=so:r,p:all,a:all&start={start}")
            html = response.text
            soup = BeautifulSoup(html,'html.parser')
            titles=soup.select(".news_tit")
            for title in titles:
                print(title.text)

            print(f"{str*20}{idx+1}번 페이지{str*20}")
    print()