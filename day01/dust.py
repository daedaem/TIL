import requests
from bs4 import BeautifulSoup

"""
$ pip install beautifulsoup4 requests lxml
"""

KEY = 'o5ALCxVrS%2BFWQWlBTd749EcD6I5KPjUvQcqMFZPXlcRlwn8FqGgNlry4mGnxnsND%2B4QO4AEwxRfnHeiZqE3Xsw%3D%3D'
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={KEY}&numOfRows=10&pageNo=3&sidoName=서울&ver=1.0'
# print(url)
response = requests.get(url).text
data = BeautifulSoup(response, 'xml')
# print(data)
item = data('item')[7]
time = item.dataTime.text
station = item.stationName.text
dust = int(item.pm10Value.text)

print(f'{time} 기준 {station}의 미세먼지 농도는 {dust} 입니다.')

# 미세먼지 농도에 따라서
# 기상청에서 등록한 수치에 따라 좋음부터 매우 나쁨까지를 출력할 수 있는
# 조건문을 만드는게 (dust에 담겨 있음)
# 

if 150 < dust : 
    print('매우나쁨')
elif 80 < dust <= 150 :
    print('나쁨')
elif 30 < dust <= 80 :
    print('보통')
else :
    print('좋음')

