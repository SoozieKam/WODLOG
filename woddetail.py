import csv

import requests
from bs4 import BeautifulSoup as bs

# 크롤링 시 기기 차단 우회하기 위함
# 랜덤한 사용자 에이전트 문자열을 생성.
# 사용자 에이전트 문자열이란? 웹 브라우저 또는 다른 HTTP 클라이언트가 웹 서버에 요청을 보낼 때 자신을 식별하기 위해 사용되는 문자열
from fake_useragent import UserAgent

# 보안 관련 모듈
import ssl

# HTTPS 연결 시 SSL 인증서 검증을 비활성화
ssl._create_default_https_context = ssl._create_unverified_context

# UserAgent 클래스의 인스턴스를 생성
user_agent = UserAgent()

# 생성된 랜덤 사용자 에이전트 문자열을 HTTP 요청의 헤더에 추가합니다.
# 이렇게 함으로써, 웹 서버로 보내는 요청이 특정한 브라우저나 디바이스에서 보내는 것처럼 보이도록 설정할 수 있습니다.
# 일부 웹 사이트는 사용자 에이전트를 통해 스크래핑을 감지하거나 제어할 수 있기 때문에, 더욱 실제 사용자와 유사한 요청을 보내기 위해 사용됩니다.
headers = {"User-Agent": user_agent.random}

page = requests.get("https://wodwell.com/wod/dt", headers=headers).text
soup = bs(page, "html.parser")

wodname = soup.find("h1", {"class": "wod-title"})
wod_detail = soup.find("ul", {"class": "workout-list"})

if wod_detail:
    li_tags = wod_detail.find_all("li")

    if li_tags:
        for li_tag in li_tags:
            li_text = li_tag.text.strip()
            print(li_text)
        else:
            print("와드 내용이 없습니다.")
print(wodname)
