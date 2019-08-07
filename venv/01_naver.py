# Client Side
# Front end
# 웹 브라우저에서 동작하는 코드를 작성하는 것

# HTML : 문서(한 화면)  프레임, 컨텐츠
# HyerTextMarkup Language
# CSS : Cascade Style Sheet , 폰트 , 글씨색 , 프레임의 굴기 , 색상
# Java Script : 동작을 담당
# + 컨텐츠를 갱신하는데 쓰임

# 웹 크롤러 - 웹 브라우저를 흉내내서 웹 서버에서 데이터를 찾고 다운받는 프로그램
# 네이버 , 구글 - 검색앤진
# 암표 매매상
# 업무 자동화- 마케팅

# 1. requests, Beautifulsoup
# 2. 로그인, 서버차단 피하기
# 3. 웹 브라우저를 제어하기 - Selenium

# !!! 네이버에서 실시간 급등 검색어 찾아오기
# 1. 내가 얻고자 하는 데이터가 있는 웹페이지의 URL 설정
url = "https://www.naver.com/"

# 2. 해당 주소를 이용해 서버에 접속해서 데이터를 얻어온다
# requests 모듈
# pip install requests
# 모듈과 프레임 웍의 차이
# 모듈 - 내가 뭔가를 필요로할때 가져야 쓰는 도구 - 내가 결과물을 만들때 중간정도의 역할만 해줌
# 프레임웍 - 너가 만약에 전을 먹고 싶으면 이대로 해야되 -->
import requests
#get, post, put, delete
# url 을 이용해서 서버에서 데이터 얻기
data = requests.get(url)

# 접속이 잘 되었는지 확인
if data.status_code != requests.codes.ok:
    print("접속 실패")
    exit()

# 접속성공
# 얻어온 데이터를 해석
# Beautiful Soup : text 를 html로 해석해주는 모듈
# pip install beautifulsoup4
# 내가 무엇을 할지 알고 해야 함 --> 코드가 막히는 사례  --> 내가 무엇을 해야 할지 몰라서 막히는 경우가 대부분
from bs4 import BeautifulSoup
html = BeautifulSoup(data.text, "html.parser")
print(html)

# 얻어낸 html 에서 원하는 요소를 찾기
# 셀렉터이용
"""
단일 셀렉터
tag : span
id(주민번호)  :  똑같은 아이디가 있으면 안됨   #ah_k
class(별명, 그룹명) : 같은 것이 존재할 수 있음 : .ah_k

복합선택자
span.ah_k
div > .ah_k
.class_e > .ah_k   ---> > : ... 안에  ... 를 찾아줘라

가방 > 지갑 > 카드 (o)  -> 대용량 어플리케이션 개발시에 이용
가방 > 카드 (x)
가방 지갑 카드 (o)
가방 카드 (o)
꺽쇠는 중간경로 생략이 불가능

"""

tags = html.select(".PM_CL_realtimeKeyword_list_base .ah_a")

for tag in tags:
    link = tag.attrs['href']
    rank = tag.select_one(".ah_r").text
    keyword = tag.select_one(".ah_k").text
    print(rank, keyword, link)
    # tag.attrs['class']
    # tag.text
    #print(tag.text)

    # iamlols -> 강사님 카카오
    # youtube -> www.actingprogrammer.tv

    # 1. 소스코드만 복사
    # 2.requirement.txt
    #
















