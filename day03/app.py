# Flask 불러옴
# Flask는 파이썬이 기본적으로 가지고 있는 모듈이 아님.
# 그럼 설치해야한다.
# 설치는 pip 라고 하는 파이썬 패키지 관리를 통해서 한다.
# pip install Flask -> bash창에 입력해서 설치한다.

from flask import Flask, render_template, request
import requests

 # 내 챗봇 토큰 필요
TOKEN = '1857659333:AAFYxTTlDXl9udlbPE52objZz5mDPYS4e5g'
    # 요청 통합 url 변수에 담기
url = f'https://api.telegram.org/bot{TOKEN}'


app = Flask(__name__)
#app을 통해 실행시킬건데 
# @(decorator)
@app.route("/")
# def로 함수를 정의
def hello_world():
# 함수 정의할 때는 vvvv 함수():
# return은 함수 반환, 함수 실행 종료 
    return "<p>Hello, World!</p>"

# return을 하는 함수가 있고 안하는 함수가 있다
# 파이썬의 모든 함수는 반환안하면 none이라고 뜸

# /ssafy -> hello, SSAFY
# Flask로 어떤 문서를 응답할때, return에 작성하는 것이 아니라,
# 특정 문서 자체를 불러와서 응답해줄 수 있다.
# render_template
# flask가 가지고 있는 함수 render_template를 불러와야 한다.
# 이거 위에 있지 않나?
# from flask import render_template를 빼고 맨 위에
# from flask import Flask, 뒤에 붙여라
# html문서 하나 만들건데 그 문서를 보여주는 페이지 만들기
@app.route('/ssafy')
def ssafy():
    # ssafy.html을 rendering 한다.
    return render_template('ssafy.html')

# 로그인이든 아니면 채팅이든
# 내가 입력한 값을 보낼 수 있는
# 메시지를 보낼 수 있고
# 보내온 메시지를 받아서 어떤 행위를 실행하는 코드
# 함수가 2개가 필요하다.

# write 함수(메세지를 입력하는 곳), send(메시지를 받는 곳)
@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    # 사용자가 요청보낸 정보 확인할 수 있는 request 불러온다.
    # from flask import reuqest -> 최상단에 작성
    # print(request)
    # <Request 'http://127.0.0.1:5000/send?message=안녕하세요' [GET]>
    # print(dir(request))
    message = request.args.get('message')
    # 텔레그램 챗봇 api url 필요
    # 메세지 보낼 사람 chat_id 필요
    chat_id = 1851824951
    send_message_url = f'{url}/sendMessage?chat_id={chat_id}&text={message}'
    # 파이썬으로 요청 보내는 requests 필요
    requests.get(send_message_url)
    return render_template('send.html')

# 주소 함수 이름이랑 동일하게 작성한다.
# html 이름도 함수 이름이랑 동일하게 작성한다
# 안의 내용은 일단 제목만 입력해서 
# 두 페이지 정상 작동하는지 확인.


# post 방식의 요청만 받겠다.
@app.route('/telegram', methods=['POST'])
def telegram():
    # 요청 정보는 request에 들어 있다.
    response = request.get_json()
    print(response)
    # reponse에 chat_id, text 들어 있다.
    #1.
    # 사용자가 챗봇한테 보낸 메시지 똑같이 돌려보내주는 코드
     #2.
    # text에 들어있는 값이 '누구야' 일 때,
    # 저는 ~의 챗봇입니다.
    # if text == "누구야?":
    #     answer = "저는"
    #     send_message_url = 
    #     requests
    response = request.get_json()
    # print(response)
    chat_id = response['message']['from']['id']
    text = response['message']['text']
    
    if text == "누구야?":
        text = "저는 조해성님의 챗봇입니다."
    #사용자가 보내온 메시지가 '미세먼지'일때만,
    # 3.작성한 미세먼지 API 코드도 같이
    # 가지고 오셔서 '미세먼지'라고 입력 받으면
    # 미세먼지 정보를 알려주는 코드도 작성해볼게요.
    elif text == '미세먼지':
        key = '3LY%2FPwYwedmnm6EKgl9Df3QPV3sr33RUxCmYYOnZ6uMVCV1Ph70%2Fd38HCh0k83eFKQlpAtCbWzqRyp%2FUhfpk5g%3D%3D'
        sidoName = '부산'
        dust_url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?service{key}&returnType=json&numOfRows=100&pageNo=1&sidoName={sidoName}%EB%B6%80%EC%82%B0&ver=1.0'
        response = requests.get(dust_url).json()
        # print(response)
        sido_name = response['response']['body']['items'][1]['sidoName']
        station_name = response['response']['body']['items'][1]['stationName']
        dust = response['response']['body']['items'][1]['pm10Value']
        text = (f'{sido_name}시 {station_name}의 미세먼지 농도는 {dust}입니다')

    send_message_url = f'{url}/sendMessage?chat_id={chat_id}&text={text}'
    requests.get(send_message_url)
    return '', 200

    
    # text에 들어 있는 값이 무엇인지에 따라서
    # 보낼 메시지 바꿔주면 된다.
    # 조건문을 넣어주면 될 것 같다.
    
    #응답은 본문과 status_code 200을 같이 보내준다.


if __name__ == '__main__':
    app.run(debug=True)




