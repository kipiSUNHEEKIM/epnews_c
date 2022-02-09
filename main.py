import requests
from bs4 import BeautifulSoup
import json
import os
import sys

# 특허뉴스(www.e-patentnews.com) 크롤러

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 연도, 주기 설정
# year = 2022 # 연도
# cycle = 4 # 주기 (ex. 분기별 = 4, 매달 = 12)
# start = 1 # 기준일 (ex. 분기별 2분기 = 2, 매달 5월 = 5)

# --------------------- 검색어 : IP5
print('특허뉴스(www.e-patentnews.com) 뉴스기사 스크래핑 시작 (검색어 : IP5)')

req = requests.get('http://www.e-patentnews.com/search.html?submit=submit&search=IP5&imageField3.x=0&imageField3.y=0&search_and=1&search_exec=all&search_section=all&news_order=1&search_start_day=&search_end_day=20220207')
req.encoding= None
html = req.content
soup = BeautifulSoup(html, 'html.parser')
datas = soup.select(
    'div.search_result_list > div.search_result_list_box > dl > dt'
    )
data = {}

for title in datas:
    name = title.find_all('a')[0].text
    url = 'http:www.e-patentnews.com/'+title.find('a')['href']
    data[name] = url

with open(os.path.join(BASE_DIR, 'e-patentNews_IP5.json'), 'w+',encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii = False, indent='\t')

print('특허뉴스(www.e-patentnews.com) 뉴스기사 스크래핑 끝 (검색어 : IP5)')

# --------------------- 검색어 : EUIPO

print('특허뉴스(www.e-patentnews.com) 뉴스기사 스크래핑 시작 (검색어 : EUIPO)')

req = requests.get('http://www.e-patentnews.com/search.html?submit=submit&search_and=1&search_exec=all&search_section=all&news_order=1&search=EUIPO&imageField.x=0&imageField.y=0')
req.encoding= None
html = req.content
soup = BeautifulSoup(html, 'html.parser')
datas = soup.select(
    'div.search_result_list > div.search_result_list_box > dl > dt'
    )

data = {}

for title in datas:
    name = title.find_all('a')[0].text
    url = 'http:www.e-patentnews.com/'+title.find('a')['href']
    data[name] = url

with open(os.path.join(BASE_DIR, 'e-patentNews_EUIPO.json'), 'w+',encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii = False, indent='\t')

print('특허뉴스(www.e-patentnews.com) 뉴스기사 스크래핑 끝 (검색어 : EUIPO)')

# --------------------- 검색어 : JPO

print('특허뉴스(www.e-patentnews.com) 뉴스기사 스크래핑 시작 (검색어 : JPO)')

req = requests.get('http://www.e-patentnews.com/search.html?submit=submit&search=JPO&imageField3.x=0&imageField3.y=0&search_and=1&search_exec=all&search_section=all&news_order=1&search_start_day=&search_end_day=20220207')
req.encoding= None
html = req.content
soup = BeautifulSoup(html, 'html.parser')
datas = soup.select(
    'div.search_result_list > div.search_result_list_box > dl > dt'
    )

data = {}

for title in datas:
    name = title.find_all('a')[0].text
    url = 'http:www.e-patentnews.com/'+title.find('a')['href']
    data[name] = url

with open(os.path.join(BASE_DIR, 'e-patentNews_JPO.json'), 'w+',encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii = False, indent='\t')

print('특허뉴스(www.e-patentnews.com) 뉴스기사 스크래핑 끝 (검색어 : JPO)')

# --------------------- 검색어 : CNIPA

print('특허뉴스(www.e-patentnews.com) 뉴스기사 스크래핑 시작 (검색어 : CNIPA)')

req = requests.get('http://www.e-patentnews.com/search.html?submit=submit&search_and=1&search_exec=all&search_section=all&news_order=1&search=CNIPA&imageField.x=0&imageField.y=0')
req.encoding= None
html = req.content
soup = BeautifulSoup(html, 'html.parser')
datas = soup.select(
    'div.search_result_list > div.search_result_list_box > dl > dt'
    )

data = {}

for title in datas:
    name = title.find_all('a')[0].text
    url = 'http:www.e-patentnews.com/'+title.find('a')['href']
    data[name] = url

with open(os.path.join(BASE_DIR, 'e-patentNews_CNIPA.json'), 'w+',encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii = False, indent='\t')

print('특허뉴스(www.e-patentnews.com) 뉴스기사 스크래핑 끝 (검색어 : CNIPA)')

# --------------------- 검색어 : USPTO

print('특허뉴스(www.e-patentnews.com) 뉴스기사 스크래핑 시작 (검색어 : USPTO)')

req = requests.get('http://www.e-patentnews.com/search.html?submit=submit&search=USPTO&imageField3.x=0&imageField3.y=0&search_and=1&search_exec=all&search_section=all&news_order=1&search_start_day=&search_end_day=20220207')
req.encoding= None
html = req.content
soup = BeautifulSoup(html, 'html.parser')
datas = soup.select(
    'div.search_result_list > div.search_result_list_box > dl > dt'
    )

data = {}

for title in datas:
    name = title.find_all('a')[0].text
    url = 'http:www.e-patentnews.com/'+title.find('a')['href']
    data[name] = url

with open(os.path.join(BASE_DIR, 'e-patentNews_USPTO.json'), 'w+',encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii = False, indent='\t')

print('특허뉴스(www.e-patentnews.com) 뉴스기사 스크래핑 끝 (검색어 : USPTO)')

