# 아래 라이브러리 설치하고 진행할 것.
# pip install beautifulsoup4 
# pip install selenium
# !apt-get update
# !apt install chromium-chromedriver
# !cp /usr/lib/chromium-browser/chromedriver /usr/bin


from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import urllib.parse
import re

def cheecker_naver(input):
    #코랩은 아래와 같이 진행주어야함. 코랩이 아닌 경우 아래 코드 주석처리할 것
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')        # Head-less 설정
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome('chromedriver', options=options)

    ##############################################################################
    baseUrl = 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query='
    plusUrl =  input.strip('')

    # 한글 검색 자동 변환
    url = baseUrl + urllib.parse.quote_plus(plusUrl)
    html = urlopen(url)
    bsObject = bs(html, "html.parser")
    li_list = []
    li_list = bsObject.find_all('div', class_ = 'suggest_wrap') 

    #수정 검색어를 제외하고 나머지 부분  제거. 
    output = ''
    for i in li_list:
        remove = re.sub("제안도움말","",i.get_text())
        remove_1 = re.sub("검색하시겠습니까","",remove)
        remove_2 = remove_1.replace(' ?','').strip('')
        remove_3 = re.sub("검색한 결과입니다.","",remove_2)
        remove_4 = re.sub("검색결과 보기","",remove_3)
        remove_5 = re.sub(plusUrl,"",remove_4).strip()
        output = remove_5.rstrip('으로')

    return output
    