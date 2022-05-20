
#문자열 데이터 타입

# print("문자열") string
print("Hello world")
print('Hello world')

#줄바꾸는 방법

#큰 따옴표3개해도 같은 방식으로 줄바꿈이 가능함
print('''
Hello
world''')


print("'1'+'1'", '1'+'1')
print('Hello woeld'*1000)
print("len('Hello woeld'*1000)", len('Hello woeld'*1000))

# 문자를 다른 문자로 치환할 때 사용하는 방법
#ex (world-> universe)
print("'Hello world'.replace('world', 'universe'", 'Hello world'.replace('world', 'universe'))


#리스트 데이터 타입
students = ["egoing", "sori", "maru"]
grades = [2,1,4]
# sori를 불러오고 싶을 때 아래처럼 코딩
print("students[1]", students[1])
# 리스트가 몇개의 원소로 이루어져 있는지 (원소= ex "egoing") 알고싶을 때
print("len(students)", len(students))

#리스트 안의 가장 작은 숫자를 찾을 때 min 제일 큰수는 max 사용
print("min(grades)", min(grades))
print("max(grades)", max(grades))
print("sum(grades)", sum(grades))

#통계와 관련된 모듈을 로딩 import statistics 평균은 maen
import statistics
print("statistics.mean(grades)", statistics.mean(grades))

# 무작위로 추첨을해서 데이터 타입중에 고르고 싶다면 random 사용
import random
print("random.choice(students)", random.choice(students))

#변수에 대한 공부 변수를 넣고 출력
name = 'sori'
print('hi '+name+' .... bye, sori')
message = 'hi, '+name+' .... bye, '+name+'.'
print(message)

#예상치 못한 오류를 버그라고 하고 그것을 고치는것을 디버그 라고한다

