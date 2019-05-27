import requests
import bs4

res = requests.get('https://finance.naver.com/marketindex/').text
#print(res)

#pip install bs4
text = bs4.BeautifulSoup(res,'html.parser')

kospi - text.select_one('#exchangeList > li.on > a.head.usd > div > span.value')

#print(kospi.text)

