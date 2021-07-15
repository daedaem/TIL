import requests

name = 'eric'
url = f'https://api.agify.io/?name={name}'
# .text == str
# response = requests.get(url).text
# print(response)
# json() -> dict
response = requests.get(url).json()
print(response)

# name의 나이는 age입니다.
name = response['name']
age = response['age']
print(f'{name}의 나이는 {age}살입니다.')