import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/search?q=%EB%B9%84%ED%8A%B8%EC%BD%94%EC%9D%B8+%ED%98%84%EC%9E%AC+%EC%8B%9C%EC%84%B8&sxsrf=ALeKk027ateqWn_SRaFEQzE0hxHjkTBfzg%3A1626316965791&ei=paDvYKrGL6rDmAWT3IiQCA&oq=%EB%B9%84%ED%8A%B8%EC%BD%94%EC%9D%B8+%ED%98%84%EC%9E%AC+%EC%8B%9C%EC%84%B8&gs_lcp=Cgdnd3Mtd2l6EAMyAggAMgQIABAeMgYIABAIEB46BwgjELADECc6BwgAEEcQsAM6BAgjECc6BwgAEIcCEBQ6BQgAELEDSgQIQRgAUMkcWO4mYMQnaANwAngBgAG3AogB7gySAQgwLjEwLjAuMZgBAKABAaoBB2d3cy13aXrIAQXAAQE&sclient=gws-wiz&ved=0ahUKEwjqrKbohuTxAhWqIaYKHRMuAoIQ4dUDCA4&uact=5'
response = requests.get(url).text
data = BeautifulSoup(response, 'html.parser')

data.select_one('#knowledge-currency__updatable-data-column > div.b1hJbf > div.dDoNo.ikb4Bb.gsrt.gzfeS > span.DFlfde.SwHCTb')
price = data.select_one('#knowledge-currency__updatable-data-column > div.b1hJbf > div.dDoNo.ikb4Bb.gsrt.gzfeS > span.DFlfde.SwHCTb')
result = price.text

print(f'현재 비트코인 시세는 {result} 입니다.')