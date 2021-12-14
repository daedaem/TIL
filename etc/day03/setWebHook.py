# setWebHook 요청 보내야 한다.
import requests

# token, url, ngrok url
TOKEN = '1857659333:AAFYxTTlDXl9udlbPE52objZz5mDPYS4e5g'
    # 요청 통합 url 변수에 담기
url = f'https://api.telegram.org/bot{TOKEN}'
# ngrok http 5000 -> https://url 복사 -> ctrl + c아님 우클릭
ngrok_url = 'https://7efed12571a4.ngrok.io'
python_anywher = 'https://tg8685.pythonanywhere.com'
set_webhook_url = f'{url}/setWebHook?url={python_anywher}/telegram'
#telegram이 내 ngrok/telegram으로 요청을 보내고 200응답받아간다.
response = requests.get(set_webhook_url)
print(response.text)