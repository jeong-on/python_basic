import requests
from bs4 import BeautifulSoup
# html parser

url = "https://movie.naver.com/movie/running/current.nhn"
result = requests.get(url)
#print(result.content)
# result

content = BeautifulSoup(result.content, "html.parser")
# content  => dom tree형태로 데이터를 가져옴
# html document

# content

dt_list = content.findAll("dt", {"class":"tit"})
# # dt_list : ResultSet class의 객체, LIST의 상속!
# # 인덱싱과 슬라이싱이 된다.
#
# print(type(dt_list)) # ResultSet이라는 클래스 객체로 넘어옴.
# 인덱싱을 가졌다.
# print(dt_list) # 전체 목록 프린트.
# print('리스트의 개수  >> ',len(dt_list)) # 글자수도 len으로 샐 수 있음.
# print(dt_list[0])
#
tag = dt_list[0].find("a") # dt_list[0]에서 a라는 태그를 찾는 함수 find
#
# print(tag)
# print(type(tag))
# print(tag.text) # a태그 안에 들어있는 텍스트

span_list = content.findAll("span", {"class":"num"})
print(span_list)
print(span_list[0])

numtag = span_list[0]
print(numtag)
print(type(numtag))
print(numtag.text)

test_list = [1,2,3]
for item in test_list:
    print(item)

for index in range(0, len(test_list)): # 0~2
    print(test_list[index])

print('=============================')

for tag in span_list:
    print(numtag.tag)

for index in range(0, len(span_list), 2): # 0~2
    print(index, ':', span_list[index].text)

print('=============================')

title_list = []
for tag in dt_list:
    print(tag.find('a').text)
    data = tag.find('a').text
    title_list.append(data)
print(len(title_list))
print(title_list)

jumsu_list = []
for index in range (0, 145):
    data = span_list[index].text
    jumsu_list.append(data)
print(len(jumsu_list))
print(jumsu_list)

title_list2 = tuple(title_list)
print(title_list2)

jumsu_list2 = tuple(jumsu_list)
print(jumsu_list2)

import mysql_movie.mysql_crud as db
db.create(jumsu_list2)