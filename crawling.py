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

page = requests.get("https://wodwell.com/", headers=headers).text
soup = bs(page, "html.parser")

# elements = soup.select("div.WodPreview_wod-title__2mhK8 h2")

all_target_divs = soup.find_all("div", {"class": "WodPreview_wod-title__2mhK8"})[:10]
all_wod_details = soup.find_all("p", {"class": "WodPreview_workout__3q6fJ"})[:10]

print(all_wod_details)

for target_div in all_target_divs:
    h2_tag = target_div.find("h2").text
    if h2_tag:
        print(f"와드명:{h2_tag}")

    else:
        print("해당 div 내에 h2 태그 없음")
    print("-" * 20)  # 구분선


for wod_details in all_wod_details:
    span_tag = wod_details.find_all("span")
    if span_tag:
        for tag in span_tag:
            tag = tag.text
            print(f"와드 내용:{tag}")


# wodnames = soup.find_all("div", {"class": "WodPreview_wod-title__2mhK8"})[:20]
# woddetails = soup.find_all("p", {"class": "WodPreview_workout__3q6fJ"})[:20]


# for index, element in enumerate(wodnames, 1):
#     print("{} 번째 와드 제목: {}".format(index, element.text))

# for index, element in enumerate(woddetails, 1):
#     print("{} 번째 와드 내용: {}".format(index, element.text))
