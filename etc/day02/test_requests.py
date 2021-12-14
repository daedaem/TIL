# 파이썬으로 요청 보내기 위한 준비
# requests라는 모듈을 사용
# 그러기 위해 불러온다.
import requests
#requests로 https://www.naver.com으로 요청 보낸 결과 출력
print(requests.get('https://www.naver.com'))

"""HTTP 200 ok는 요청이 성공했음을 나타내는 성공 읍답상태 코드
    2로 시작하는 건 보통 성공
인터넷 창 안열렸을 때 'page not found 404'
    권한 없거나 없는 페이지는 보통 4로 시작
server error 503
    서버터졌을 때는 5로 시작함
"""

# alt + 방향기 위 아래로 한줄 복사 
print(requests.get('https://www.naver.com').text)
print(requests.get('https://www.naver.com').status_code)
