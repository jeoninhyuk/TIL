# import requests
# from bs4 import BeautifulSoup
#
# html = requests.get('https://www.naver.com/').text
# soup = BeautifulSoup(html, 'html.parser')
#
# title_list = soup.select('.PM_CL_realtimeKeyword_rolling span[class*=ah_k]')
#
# for idx, title in enumerate(title_list, 1):
#     print(idx, title.text)
##################################################################################
import requests
import bs4
import datetime

html = requests.get('https://www.naver.com/').text
soup = bs4.BeautifulSoup(html, 'html.parser')

ranks = soup.select('.PM_CL_realtimeKeyword_rolling .ah_item .ah_k')
now = datetime.datetime.now()

with open('naver_rank.txt', 'w', encoding='utf-8') as f:
    f.write(f'{now} 기준 네이버 검색어 순위\n')
    for i, rank in enumerate(ranks):
        f.write(f'{i+1}.{rank.text}\n')