#- 언어의 인기

#- shell
#    - 간단한 일
#    - interactive mode
#    - 대화하듯이 사용
#    - ;로 구분하여 사용 가능
#    - \는 실행 유보
#    - 위쪽 화살표 키 누르면 전에 사용했던 명령어 사용 가능
#    - 콘솔에서 빠져나갈 때는 exit() 사용
#- file
#    - 자주 시키는 일 순서대로 적어놨다가 사용 / 복잡한 일
#
#- python 혹은 python3 입력해 사용
#    - >>> “ prompt(우리가 명령어 입력하는 곳)

print(1+1)
a = 1 
b = 1
print(a+b)

# data type에 따라 연산 방식 다름 
# python에 매우 강력한 계산 기능 내장됨
# number - 정수형, 실수형

# 정수
print(-1)
print(0)
print(1) # int = 정수

# 소수
print(1.1) #float = 실수 
print('1+1',1+1)
print('2-1', 2-1)
print('2*2', 2*2)
print('2/2', 2/2)

import math
print('math.sqrt(4)', math.sqrt(4))
print('math.pow(4,2)', math.pow(4,2))

import random
print('random.random()',random.random())

print('hello world')
print("hello world")
print('''
hello
world
''')

# ''' : 길어졌을 떄 줄 바꿈 되도 text로 인식 될 수 있게 해줌 

print("'1'+'1'",'1'+'1') 

print('hello world'*1000)
print(len('hello world'*1000))
print('hello world'.replace('world', 'universe')) # replace : 텍스트 교체 

#list : 성격 비슷한 것들끼리 묶음. []로 묶음 그 속에 element들은 ,로 구분

students = ["egoing", "sori", "maru"]
grades = [2, 1, 4]

print(students[1])
print(grades[0])

print(len(students))

print(min(grades)) # min : 최솟값
print(max(grades)) # max : 최댓값

import statistics
print(statistics.mean(grades))

import random
print(random.choice(students))

#숫자, 문자, 리스트 / 데이터 타입 3가지

price = 10000
vat_rate = 0.1 #vat = tax

vat = price * vat_rate
print(vat)

name = input('name: ')
message = print('hi, '+name+' ... bye, '+name+'.')
print(message)

#debug : 버그를 없애는 것 
#debugger : 프로그램 중지시키고 한줄 한줄 변화 파악 가능 
#input -> process -> output

import pandas as pd 
assignment = pd.read_csv('assignment.csv')
print(assignment)

print(assignment.describe()) # min, mean, max 등 다양한 값 뽑아줌


# 제어문 


