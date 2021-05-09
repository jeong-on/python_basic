import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekdayList.nhn?week=fri"
result = requests.get(url)

content = BeautifulSoup(result.content, "html.parser")

web_list = content.findAll("dl")
# print(len(web_list))
# print(web_list[0])

# 웹툰 제목
title = []
for i in range(len(web_list)):
    title_data = web_list[i].find("a").text
    title.append(title_data)
print(title)
print(len(title))

print('================================')

print(web_list[0])

print('================================')

# 웹툰 작가 이름
name_list = content.findAll("a",{"class":"author"})
print(name_list)
print(len(name_list))

name = []
for i in range(len(name_list)):
    name_data = name_list[i].text
    name.append(name_data)
print(name)
# print(len(name))
#
# star = web_list[0].findAll("strong")
# print(star[1].text)
