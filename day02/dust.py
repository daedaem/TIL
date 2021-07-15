# sido_name의 미세먼지 농도는 dust 입니다. 출력
# pm10Value

import requests
key = '3LY%2FPwYwedmnm6EKgl9Df3QPV3sr33RUxCmYYOnZ6uMVCV1Ph70%2Fd38HCh0k83eFKQlpAtCbWzqRyp%2FUhfpk5g%3D%3D'
# 사용자가 입력한 값으로 요청을 보내보자.
# 사용자가 값을 입력할 수 있는 방법이 필요하다.
sido_name = input('전국, 서울, 부산, 대구, 인천, 광주, 대전, 울산, 경기, 강원, 충북, 충남, 전북, 전남, 경북, 경남, 제주, 세종 중에서 선택해주세요')
url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?service{key}}&returnType=json&numOfRows=100&pageNo=1&sidoName={sidoName}%EB%B6%80%EC%82%B0&ver=1.0'
# print(url)
response = requests.get(url).json()
# print(response)
# items = response['response']['body']['items'][1]['sidoname']]
sido_name = response['response']['body']['items'][1]['sidoName']
station_name = response['response']['body']['items'][1]['stationName']
dust = response['response']['body']['items'][1]['pm10Value']

# for value in items:
    # if value['stationName'] == station_user_input:
        # sido_name = value['sidoName']


print(f'{sido_name}시 {station_name}의 미세먼지 농도는 {dust}입니다.')

