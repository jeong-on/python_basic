# 기본형 4가지
# 정수, 실수

age = 100
weight = 99.9

sum = age + weight # 더하기 연산자(하나라도 스트링이 들어가면 결합연산자)
print(sum)

# 문자

# 논리
temp = '못봄'
temp2 = float(temp)
print (type(temp2))

if temp2 == temp:
    print('못봄')

# 타입을 변경하는 것 : 형변환(casting, 캐스팅)
# 문자로 변경하는 것 : str()
# 정수로 변경하는 것 : int()
# 실수로 변경하는 것 : float()

# 문자
# String을 의미, char를 포함하는 의미!
company = '메가'
print (company) # print후 enter추가(println)
print ('우리 회사는',company)

# 논리
food = True # False(첫글자는 대문자로 작성)
food2 = 1

if food == food2: # == True: (True는 생략 가능, 비교연산자 == 사용
    print ('배가 부르시겠군요.!')
else:
    print ('배가 고파요!')
