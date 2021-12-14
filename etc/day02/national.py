# requests를 불러옴
import requests

# 요청 보낼 url 작성
name = 'joe'
url = f'https://api.nationalize.io/?name={name}'

# 이름과 함께 요청을 보낸다.
# 응답받은 값을 json 함수를 통해 dcit로 변환한다.
response = requests.get(url).json()
# 응답받은 결과의 형태를 확인하고,
# print(response)

#첫번째 결과물에서 국가명과 확률을 뽑는다.
country_id = response['country'][0]['country_id']
# 유사도 소수를 변경해서 퍼센티지 형태로 변환한다.
    # 곱셉은 *를 활용한다.
probability = response ['country'][0]['probability'] * 100
# 소수점 형태의 문자열
print(country_id, probability)
name = response['name']

# round - 내장함수로 반올림 가능하다.
# round(float, 반올림하고자 하는 위치)
print(f'{name}의 국가는 {round(probability, 2)}% 확률로 {country_id}입니다.')
