# 변수
aaa = 1
bb = True
b = "안녕"

# 변수명 =
# 수학 = 같다의미, 프로그래밍 = 할당(오른쪽에 있는 것을 왼쪽으로 할당_ex. 10=c -불가 => c=10)
# 변수명 규칙
# 1) 대소문자를 구분함 (ex. A=100, a=10)
# 2) 변수명 : 특수문자가 올 수 없음.
# 3) 특수문자 : _ 언더바만 가능 (ex. _abc, _num, n_1 -가능)
# 4) 숫자가 제일 앞에 올 수 없음. (ex. 100top, 7up -불가)
# 5) 숫자가 중간에 오는 것은 가능. (ex. top100, up7, a1 -가능)
# 6) 예약어는 사용불가 (True, False, None, and, or, for ...), (but, true -가능, 사용지양)

a=10  #변수만 변경하면 값을 다 변경할 필요x
b=5
# print
print(10+5) #print(a+b)
print(10-5) #print(a-b)
print(10*5) #print(a*b)
print(10/5) #print(a/b)

# 타입 = bool타입 : True, False / int타입: 정수 / float타입: 실수 / str타입: 문자열
aaa = True
bbb = False
ccc = 100
ddd = 0.1
eee = "안녕"
print(type(aaa)) # bool타입
print(type(ccc)) # 숫자 - 정수
print(type(ddd)) # 숫자 - 실수
print(type(eee)) # 문자열
