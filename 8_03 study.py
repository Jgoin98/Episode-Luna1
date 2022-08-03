# 숫자형 데이터 타입 int , float
print(-1)
print(0)
print(1) # 정수형 int
print(1.1) # 실수형 float
print('1+1', 1+1) # 덧셈
print('2-1', 2-1) # 뺄셈
print('2*2', 2*2) # 곱셈
print('4/2', 4/2) # 나누기

import math #수학과 관련된 여러가지 기능 모듈

print(math.sqrt(4)) #제곱근을 구하는 공식
print(math.pow(4,2)) #제곱을 구하는 공식

import random #랜덤한 숫자를 불러옴
print(random.random())

# 문자열 데이터 타입 string
print('Hello world')
print("Hello world")

# 파이썬에서 줄바꿈 하는법 (큰따옴표도 사용가능)
print('''
Hello
world
''')

# 숫자에 큰,작은 따옴표 사용시 문자열로 인식한다
print('1'+'1', '1'+'1')

# 문자열 연산자에 곱하기 사용하여 여러번 실행가능
print('Hello world'*10)
# 문자가 총 몇글자인지 확인할 때 사용
print(len('Hello world'*10))

# 리스트 데이터 타입 list (주의해야할점 파이썬에서 첫시작은 0번째로 시작된다)
students = ["egoing", "sori", "maru"]
grades = [2,1,4]
print(students[1])
# 리스트가 몇개의 원소로 이루어져 있는지 확인할 때 (이때는 1번째 부터 시작)
print(len(students))
# 가장 작은값이 뭔지 알고 싶을 때
print(min(grades))
# 가장 큰값이 뭔지 알고 싶을 때
print(max(grades))
# 원소를 합한 값을 알고 싶을 때
print(sum(grades))

# (통계와 관련된 모듈)
import statistics
# 평균을 내고 싶을 때 
print(statistics.mean(grades))

# 랜덤으로 선택할 때
import random
print(random.choice(students))