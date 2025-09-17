# ---------------------------------
# Chapter 05 함수


# ======================================
# ----- 05-1 함수 만들기 - 매개변수 -----
# ======================================
# 함수 호출: 함수 사용한다는 뜻
# 매개변수: 함수 호출 시 괄호 내부에 넣는 자료
# 리턴값: 함수 호출 후 나오는 최종 결과

# 예제1 -- 함수 기본
# def print_3_times():
#     print("안녕하세요")
#     print("안녕하세요")
#     print("안녕하세요")
# print_3_times()

# 예제2 -- 매개변수 기본 : 함수 선언,호출 같은 개수의 매개변수 입력해야 함
# def print_n_times(value,n):
#     for i in range(n):
#         print(value)
# print_n_times("안녕하세요.",5)
# 예제3 -- 가변 매개변수 : 매개변수를 원하는 만큼 받을 수 있는 함수 - 뒤에 일반 매개변수 못 옴
# def print_n_times(n, *values):
#     for i in range(n):
#         for value in values:
#             print(value)
#         print()
# print_n_times(3, "안녕","즐거운","파이썬")
# 예제4 -- 기본 매개변수 : '매개변수=값' / 매개변수 미입력시 들어가는 기본값 - 뒤에 일반 매개변수 못 옴
# def print_n_times(value,n=2):
#     for i in range(n):
#         print(value)
# print_n_times("안녕하세요.")
# 예제5 -- 키워드 매개변수
# def print_n_times(*values,n=2):
#     for i in range(n):
#         for value in values:
#             print(value)
#         print()
# print_n_times("안녕","즐거운","파이썬",n=3)  # n=3 : 키워드 매개변수
# 예제6 -- 키워드 매개변수 - 여러 함수 호출
# def test(a, b=10, c=100):
#     print(a+b+c)
#     print(f"a: {a}\t b: {b}\t c: {c}")
# test(10,20,30)  # 기본 형태
# test(a=10, b=100, c=200)  # 키워드 매개변수
# test(c=10, a=100, b=200)  # 키워드 매개변수 마구잡이로 지정한 형태
# test(10, c=200)  # 키워드 매개변수로 일부만 지정한 형태

# 기본 매개변수 < 키워드 매개변수 (우선순위)

# ======================================
# ----- 05-1 함수 만들기 - 리턴 return -----
# ======================================
# value = input("> ")
# print(value)
# 예제1 -- 자료 없이 리턴하기
# def return_test():  # 함수 정의
#     print("A 위치입니다.")
#     return
#     print("B 위치입니다.")
# return_test()       # 함수 호출
# 예제2 -- 자료 함께 리턴하기
# def return_test():  # 함수 정의
#     return 100
# value = return_test() # 함수 호출
# print(value)
# 예제3 -- 아무것도 리턴하지 않기  => None 출력됨
# def return_test():
#     return
# value = return_test()
# print(value)
# ======================================
# ----- 05-1 함수 만들기 - 기본적인 함수 활용 -----
# ======================================
# 예제1 -- 범위 내부의 정수를 모두 더하는 함수
# def sum_all(start, end):
#     output = 0
#     for i in range(start, end+1):
#         output += i
#     return output
# print("0 to 100:",sum_all(0,100))
# print("0 to 1000:",sum_all(0,1000))
# print("50 to 100:",sum_all(50,100))
# print("500 to 1000:",sum_all(500,1000))
# 예제2 -- 기본 매개변수와 키워드 매개변수를 활용해 범위의 정수를 더하는 함수
# def sum_all(start=0, end=100, step=1):
#     output=0
#     for i in range(start, end+1, step):
#         output+=i
#     return output
# print("A.",sum_all(0,100,10))
# print("B.",sum_all(end=100))
# print("C.",sum_all(end=100, step=2))
# p291 -- 도전문제 2번
# def mul(*values):
#     output=1
#     for value in values:
#         output*=value
#     return output
# print(mul(5,7,9,10))

# ======================================
# ----- 05-2 함수의 활용 - 재귀함수 : 자기자신을 호출 -----
# ======================================
# p293 -- 예제1 -- 반복문으로 팩토리얼 구하기
# def factorial(n):
#     output=1
#     for i in range(1, n+1):
#         output*=i
#     return output
# print("1!:",factorial(1))
# print("2!:",factorial(2))
# print("3!:",factorial(3))
# print("4!:",factorial(4))
# print("5!:",factorial(5))
# 예제2 -- 재귀함수로 팩토리얼 구하기
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# print("1!:",factorial(1))
# print("2!:",factorial(2))
# print("3!:",factorial(3))
# print("4!:",factorial(4))
# print("5!:",factorial(5))
# 예제3 -- 재귀함수로 구현한 피보나치 수열(1)
# def fibonacci(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# print("1:",fibonacci(1))
# print("2:",fibonacci(2))
# print("3:",fibonacci(3))
# print("4:",fibonacci(4))
# print("5:",fibonacci(5))
# 예제4 -- 재귀함수로 구현한 피보나치 수열(2), global 키워드
# counter = 0
# def fibonacci(n):
#     print("fibonacci({})를 구합니다.".format(n))
#     global counter    # 함수 내부에서 함수 외부에 있는 변수 참조할 때 사용 (파이썬에서만)
#     counter+=1
#     if n==1:
#         return 1
#     if n==2:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# fibonacci(10)
# print("---")
# print("fibonacci(10) 계산에 활용한 덧셈 횟수는 {}번입니다.".format(counter))
# 예제5 -- 재귀함수로 구현한 피보나치 수열(3)
# counter = 0
# def fibonacci(n):
#     counter+=1
#     if n==1:
#         return 1
#     if n==2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(10))    # UnboundLocalError

# 예제6 -- 메모화 - 딕셔너리 사용해서 한번 계산한 값을 저장함(메모)
# 메모변수 생성
# dictionary  = {
#     1: 1,
#     2: 1
# }
# # 함수 선언
# def fibonacci(n):
#     if n in dictionary:
#         return dictionary[n]
#     else:
#         output = fibonacci(n-1) + fibonacci(n-2)
#         dictionary[n] = output
#         return output
# print("fibonacci(10): ",fibonacci(10))
# print("fibonacci(20): ",fibonacci(20))
# print("fibonacci(30): ",fibonacci(30))
# print("fibonacci(40): ",fibonacci(40))
# print("fibonacci(50): ",fibonacci(50))
# 예제7 -- 조기리턴
# def fibonacci(n):
#     if n in dictionary:
#         return dictionary[n]
#     output = fibonacci(n-1) + fibonacci(n-2)
#     dictionary[n] = output
#     return output

# 예제8 -- 재귀함수-리스트 평탄화하기(1)
# def flatten(data):
#     output=[]
#     for item in data:
#         if type(item) == list:
#             output+=item
#         else:
#             output.append(item)
#     return output
# example = [[1,2,3],[4,[5,6]],7,[8,9]]
# print("원본:",example)
# print("변환:",flatten(example))
# 예제9 -- 재귀함수-리스트 평탄화하기(2) - 무한히 중첩된 리스트도 다 평탄화 가능
# def flatten(data):
#     output=[]
#     for item in data:
#         if type(item) == list:
#             output += flatten(item)
#         else:
#             output.append(item)
#     return output
# example=[[1,2,3],[4,[5,6]],7,[8,9]]
# print("원본:",example)
# print("변환:",flatten(example))
# -------------
# append → 리스트 안에 리스트 자체를 넣음
# extend / += → 리스트 안에 리스트의 원소들을 펼쳐서 넣음
# -------------

# p315 -- 문제
# minimum = 2
# maximum = 10
# entire = 100
# memo = {}
# def question(left,seated):
#     key = str([left,seated])
#     # 종료 조건
#     if key in memo:
#         return memo[key]
#     if left < 0:
#         return 0
#     if left == 0:
#         return 1
#     # 재귀 처리
#     count = 0
#     for i in range(seated,maximum+1):
#         count += question(left-i,i)
#     # 메모화 처리
#     memo[key] = count
#     # 종료
#     return count
# print(question(entire,minimum))

# ======================================
# p316 ----- 05-3 함수 고급 - 튜플 : 리스트와 비슷한 자료형, 차이점: 내부요소변경 불가능 -----
# ======================================
# p318 -- 예제1 -- 리스트와 튜플의 특이한 사용
# [a,b] = [10,20]  # 리스트
# (c,d) = (10,20)  # 튜플
# print("a:",a)
# print("b:",b)
# print("c:",c)
# print("d:",d)
# 예제2 -- 괄호가 없는 튜플
# tuple_test = 10,20,30,40
# print("tuple_test:",tuple_test)  # tuple_test: (10, 20, 30, 40)
# print("type(tuple_test):",type(tuple_test))  # type(tuple_test): <class 'tuple'>
# tuple_test[0] = 55 # 내부요소 변경 불가
# print(tuple_test)  # TypeError: 'tuple' object does not support item assignment
# a,b,c = 10,20,30
# print("a:",a)
# print("b:",b)
# print("c:",c)
# 예제3 -- 변수의 값을 교환하는 튜플
# a,b = 10,20
# print("# 교환 전 값")
# print("a:",a)
# print("b:",b)
# print()
# a,b = b,a
# print("# 교환 후 값")
# print("a:",a)
# print("b:",b)
