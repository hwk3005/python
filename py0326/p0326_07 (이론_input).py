a=100
b=50
print(a) #100
print(b) #50

# Q. b=100, a=50 값을 교체 → 하려면 어떻게 값을 변경하면 될까요?
a=b
b=a
print(a) # 50
print(b) # 50

# 두 변수의 값을 교체하려면, 추가적인 변수 c를 하나두고 값을 보관해서 교체
# c=a
# a=b
# b=c

a,b=b,a # 파이썬 a,b의 변수값 교체방법
# a=b
# b=a

# 입력: input
# 출력: print
print(input("숫자를 입력하세요."))

# 변수() 있으면 함수 - 어떠한 기능구현을 말함.
print()  #함수
a        #변수

# 입력 - 무조건, 문자열(str)타입
# ★★★ 타입 변경 - 정수: int(), 실수: float(), 문자열: str()
a=input("1. 숫자를 입력하세요.")
b=input("2. 숫자를 입력하세요.")
a=int(a) #str → int
b=int(b) #str → int

a=float(a)
b=float(b)

print(a,b)
print(type(a)) # str - 문자열
print(type(b))
print(a+b) #100,500 => 100500 (+ 더하기의 의미x)

