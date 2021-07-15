# requests, bs4를 불러온다
import requests 
from bs4 import BeautifulSoup

# 요청보내기위한 url
url='https://finance.naver.com/marketindex/'

# 위url로 요청을 보낸다
response = requests.get(url).text
# print(response)

# 응답받은 문서를 파이썬이 읽을 수 있게 변환
data = BeautifulSoup(response, 'html.parser')#html 읽을 수 있도록 옵션 추가

# 변환 후, 내가 원하는 정보 부분만 선택한다.
data.select_one('#exchangeList > li.on > a.head.usd > div > span.value')
exchange = data.select_one('#exchangeList > li.on > a.head.usd > div > span.value')

# 선택한 정보중에 텍스트만 뽑는다.
result = exchange.text

# 출력한다.
# print(result)

# 현재 원/달러 환율은 result입니다.
print(f'현재 원/달러 환율은 {result} 입니다.')

