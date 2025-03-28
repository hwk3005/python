# 변수: 값을 입력할 때 타입 정의, 변수에 다시 값을 넣으면 값이 변경됨.

# Q1. 변수 선언 후 값, 타입을 출력하시오.
# a 홍길동
# b 20
# c 22.5
# d True
a="홍길동" # str
print(a)
print(type(a))
b=20 # int
print(b)
print(type(b))
c=22.5 #float
print(c)
print(type(c))
d=True # bool - True, False
print(d)
print(type(d))

num=100
print(num)
num=200
print(num)
num="안녕"
print(num)

# 변수 선언
num=0
# 변수에 값을 더해서 자신의 변수에 입력
print(num)
num=num+1
print(num)
num=num+1
print(num)

# 복합 대입 연산자
num += 1  # num = num + 1 (동일)
num -= 1  # num = num - 1
num *= 1  # num = num * 1
num /= 1  # num = num / 1


