# requests 불러오기
import requests
# pprint 이쁘게 출력
from pprint import pprint

# 봇 토큰 변수에 담기
TOKEN = '1857659333:AAFYxTTlDXl9udlbPE52objZz5mDPYS4e5g'
# 요청 통합 URL 변수에 담기
url = f'https://api.telegram.org/bot{TOKEN}'
# print(url)

# 내 챗봇에 메세지 보낸사람 정보 알아내기 (getUpdates)
get_updates_url = f'{url}/getUpdates'
# print(get_updates_url)
response = requests.get(get_updates_url).json()
# 그사람이 보낸 메시지와 그사람의 chat_id 알아내기
# print(response)
# pprint(response)
chat_id = response['result'][0]['message']['from']['id']
text = response['result'][0]['message']['text']
# print(chat_id, text)

# 메시지 보낸 사람에게
# 그 사람이 보낸 메시지 다시 돌려보내기
# sendMessage method의 필수 params(패러미터)인 chat_id인 text를 넣는다.
send_message_url = f'{url}/sendMessage?chat_id={chat_id}&text={text}'
requests.get(send_message_url)