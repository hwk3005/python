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
# p317 -- 기본
# tuple_test = (10,20,30)
# print(tuple_test[0],tuple_test[1],tuple_test[2])
# tuple_test[0] = 1   # TypeError: 'tuple' object does not support item assignment
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

# 250918
# 예제1 - 복습
# [a,b]=[10,20]
# (c,d)=(10,20)
# print(a,b,c,d)
# 예제2 - 복습
# tuple_test = 10,20,30,40
# print(tuple_test)
# print(type(tuple_test))
# a,b,c = 10,20,30
# print(a,b,c)
# 예제3 - 복습
# a,b = 10,20
# print(a,b)
# a,b = b,a
# print(a,b)

# 예제1 -- 튜플과 함수 : 여러 개의 값 리턴하기
# def test():
#     return (10,20)
# a,b = test()
# print(a,b)
# 예제2 -- 튜플 리턴하는 함수 예
# for i,value  in enumerate([1,2,3,4,5,6]):
#     print("{}번째 요소는 {}입니다.".format(i,value))
# a,b = 97,40         # 튜플x, 각각 독립된 int타입
# print(a//b,a%b)     # 튜플x
# print(divmod(a,b))  # 튜플o, divmod() 함수: 튜플형태로 몫,나머지 리턴
# x,y = divmod(a,b)   # 언패킹됨(튜플->int)
# print(x,y)          # 튜플x, int타입
# print(type(x),type(y))

# ======================================
# p322 ----- 05-3 함수 고급 - 람다 들어가기 전  -----
# ======================================
# 콜백 함수 callback function : 함수의 매개변수에 사용하는 함수
# 예제1 -- 함수의 매개변수로 함수 전달하기
# def call_10_times(func):    # "넘겨받은(매개변수) 함수를 10번 실행(호출)해주는 함수"
#     for i in range(10):
#         func()              # func() == print_hello() 함수 호출하니 print("안녕하세요")가 출력됨
# # 간단히 출력하는 함수
# def print_hello():
#     print("안녕하세요")
# # 조합하기
# call_10_times(print_hello)  

# 예제2 -- map(), filter() 함수 : map/filter(함수,리스트) : 함수를 매개변수로 사용하는 대표적인 표준함수(내장함수)
# def power(item):    # 함수 선언
#     return item * item
# def under_3(item):
#     return item < 3
# list_input_a = [1,2,3,4,5]  # 변수 선언
# # map() 함수 사용
# output_a = map(power, list_input_a)       # map(함수,리스트) → 리스트의 모든 원소에 함수를 적용
# print("map(power, list_input_a):", output_a)    # 주소값 출력됨 : 제너레이터 generator
# print("map(power, list_input_a):", list(output_a)) # 리스트 출력됨
# # filter() 함수 사용
# output_b = filter(under_3, list_input_a)  # filter(조건함수, 리스트) → 리스트의 원소 중에서 조건 함수가 True인 값만 걸러서 반환
# print("filter(under_3, list_input_a):", output_b)  # “True/False로 판별되는 값”만 보고 걸러냄
# print("filter(under_3, list_input_a):", list(output_b))
# 예제2 -- 복습풀이
# def power(item):
#     return item * item
# def under_3(item):
#     return item < 3
# list_a = [1,2,3,4,5]
# output_a = map(power, list_a)
# print("map: ",list(output_a))  # map:  [1, 4, 9, 16, 25]
# output_b = filter(power, list_a)
# print("filter: ",list(output_b)) # filter:  [1, 2, 3, 4, 5]
# # filter()가 함수의 True/False 결과값 자체를 반환하는 게 아니라,
# # 그 결과가 True인 경우에만 원래 원소를 결과에 남겨둠.
# output_a = map(under_3, list_a)
# print("map: ",list(output_a))  # map:  [True, True, False, False, False] : 3이하 값만 True로 처리
# output_b = filter(under_3, list_a)
# print("filter: ",list(output_b)) # filter:  [1, 2]

# ======================================
# p324 ----- 05-3 함수 고급 - 람다 lambda : 간단한 함수를 쉽게 선언하는 방법  -----
# ======================================
# 예제1 -- 람다 (lambda 매개변수: 리턴값)
# power = lambda x: x*x   # 함수 선언
# under_3 = lambda x: x<3
# list_input_a = [1,2,3,4,5]  # 변수 선언
# output_a = map(power, list_input_a)
# print("map(power, list_input_a):", output_a)
# print("map(power, list_input_a):", list(output_a))
# output_b = filter(under_3, list_input_a)
# print("filter(under_3, list_input_a):", output_b)
# print("filter(under_3, list_input_a):", list(output_b))
# 예제2 -- 인라인 람다
# list_input_a = [1,2,3,4,5]  # 변수 선언
# output_a = map(lambda x: x*x, list_input_a)
# print("map(power, list_input_a):", output_a)
# print("map(power, list_input_a):", list(output_a))
# output_b = filter(lambda x: x<3, list_input_a)
# print("filter(under_3, list_input_a):", output_b)
# print("filter(under_3, list_input_a):", list(output_b))

# 람다 복습
# 1) 함수 선언해서 map(), filter()
# list_input_a = [1,2,3,4,5]
# def power(item):
#     return item * item
# def under_3(item):
#     return item < 3
# output_a = map(power, list_input_a)
# print("map:",list(output_a))
# output_b = filter(under_3, list_input_a)
# print("filter:", list(output_b))

# 2) (아웃라인) 람다 사용, map(), filter()
# list_input_a = [1,2,3,4,5]
# power = lambda x: x*x
# under_3 = lambda x: x<3
# output_a = map(power, list_input_a)
# print("map: ", list(output_a))
# output_b = filter(under_3, list_input_a)
# print("filter: ", list(output_b))

# 3) (인라인) 람다 사용, map(), filter()
# list_input_a = [1,2,3,4,5]
# output_a = map(lambda x: x*x, list_input_a)
# print("map:", list(output_a))
# output_b = filter(lambda x: x<3, list_input_a)
# print("filter:", list(output_b))

# ======================================
# p326 ----- 05-3 함수 고급 - 파일처리  -----
# ======================================
# 파일 - 텍스트 파일 / 바이너리 파일
# 예제1 -- 파일 열고 닫기, open(), close() 해야 됨
# 파일 객체 = open(문자열: 파일경로, 문자열: 모드)  / *모드: w (write새로 쓰기), a (append뒤에이어서 쓰기), r (read읽기)
# file = open("basic.txt","w")    # 파일 열기
# file.write("Hello Python..!")   # 파일 텍스트 쓰기
# file.close()                    # 파일 닫기

# 예제2 -- with 키워드 - open() - close() 안해도 됨
# with open(문자열: 파일경로(파일명), 문자열: 모드) as 파일 객체: 문장
# with open("basic.txt","w") as file:
#     file.write("Hi PYTHON..!")
# 예제3 -- 텍스트 새로쓰기 write(), 텍스트 읽기 read()  # 파일객체.write/read()
# with open("basic.txt","r") as file:
#     contents = file.read()
# print(contents)
# 예제4 -- 랜덤하게 1000명의 키와 몸무게 만들기
# import random
# hanguls = list("가나다라마바사아자차카타파하")
# with open("info.txt","w") as file:
#     for i in range(1000):
#         name = random.choice(hanguls) + random.choice(hanguls)
#         weight = random.randrange(40,100)
#         height = random.randrange(140,200)
#         file.write(f"{name}, {weight}, {height}\n")
# 예제5 -- 반복문으로 파일 한 줄씩 읽기
# for 한 줄을 나타내는 문자열 in 파일객체: 처리
# with open("info.txt","r") as file:
#     for line in file:   # line: 한 줄씩 읽기
#         (name, weight, height) = line.strip().split(", ")  # p142 -- 문자열 양옆 공백제거: strip()
#         if (not name) or (not weight) or (not height):
#             continue
#         bmi = int(weight)/( (int(height)/100)**2 )  # 몸무게(kg) ÷ (키(m))² / 키(cm → m 변환) → int(height)/100
#         result = ""  # 변수 선언
#         if 25 <= bmi:
#             result = "과체중"
#         elif 18.5 <= bmi:
#             result = "정상체중"
#         else:
#             result = "저체중"
#         print("\n".join([       # "\n"엔터키로 문자열 연결
#             "이름: {}", "몸무게: {}", "키: {}", "BMI: {:.2f}", "결과: {}"
#         ]).format(name,weight,height,bmi,result) )
#         print()
# (복습) 반복문으로 파일 한 줄씩 읽기, info.txt, bmi 계산
# with open("info.txt","r") as file:
#     for line in file:
#         # 변수 선언
#         (name, weight, height) = line.strip().split(", ")
#         # 데이터에 문제 없는지 확인
#         if (not name) or (not weight) or (not height):
#             continue
#         # 결과 계산
#         bmi = int(weight) / ((int(height)/100)**2)
#         result = ""
#         if 25 <= bmi:
#             result = "과체중"
#         elif 18.5 <= bmi:
#             result = "정상 체중"
#         else:
#             result = "저체중"
#         # 출력
#         print("\n".join([
#             "이름: {}", "몸무게: {}", "키: {}", "BMI: {}", "결과: {}"
#         ]).format(name, weight, height, bmi, result))
#         print()

# ======================================
# p336 ----- 05-3 함수 고급 - 좀더알아보기 : 제너레이터  -----
# ======================================
# 제너레이터 generator (이터레이터를 직접 만들 때 사용하는 코드)
# 함수 내부에 yield 키워드 사용시 -> 제너레이터 함수됨 => 제너레이터 리턴함(리턴값(제너레이터 객체): <generator object test at 0x0000017FCDF55B40>)
# 제너레이터 객체: 함수의 코드를 조금씩 실행할 때 사용함.
# 예제1 -- 제너레이터 함수
# def test():
#     print("함수가 호출되었습니다.")
#     yield "test"
# print("A 지점 통과")
# test()
# print("B 지점 통과")
# test()
# print(test())
# (복습)
# def test():
#     print("함수가 호출되었습니다.")
#     yield "test"
# print("A 지점 통과")
# print(next(test()))
# print("B 지점 통과")
# print(test())

# 예제2 -- 제너레이터 객체와 next() 함수
# 1) 함수 선언
# def test():
#     print("A 지점 통과")
#     yield 1
#     print("B 지점 통과")
#     yield 2
#     print("C 지점 통과")
# # 2) 함수 호출
# output = test()
# print("D 지점 통과")
# a = next(output)
# print(a)
# print("E 지점 통과")
# b = next(output)
# print(b)
# print("F 지점 통과")
# c = next(output)
# print(c)        # 함수 호출 이후 yield 키워드 못 만나고 함수 끝나면 StopIteration
# next(output)

# ======================================
# p338 ----- 05-3 함수 고급 - 좀더알아보기 : 리스트함수의 key 키워드 매개변수  -----
# ======================================
# 예제1 -- min(), max() 함수 복습
# a = [52,273,32,103,57]
# print(min(a))
# print(max(a))
# 예제2 -- 키워드 매개변수에 함수 전달하기
# books = [{
#     "제목": "혼자 공부하는 파이썬",
#     "가격": 18000
# }, {
#     "제목": "혼자 공부하는 머신러닝 + 딥러닝",
#     "가격": 26000
# }, {
#     "제목": "혼자 공부하는 자바스크립트",
#     "가격": 24000
# }]
# def price_output(book):
#     return book["가격"]
# print("min:",min(books, key=price_output))
# print("max:",max(books, key=price_output))
# 예제3 -- 콜백 함수를 람다로 바꾸기
# books = [{
#     "제목": "혼자 공부하는 파이썬",
#     "가격": 18000
# }, {
#     "제목": "혼자 공부하는 머신러닝 + 딥러닝",
#     "가격": 26000
# }, {
#     "제목": "혼자 공부하는 자바스크립트",
#     "가격": 24000
# }]
# print(min(books, key=lambda book: book["가격"]))
# print(max(books, key=lambda book: book["가격"]))

# 예제4 -- sort() 정렬
# a = [52,273,103,32,57,272]
# a.sort()
# print("순차정렬:",a)
# a.sort(reverse=True)
# print("역순정렬:",a)
# 예제 5 -- 딕셔너리 오름차순 정렬하기 (가격 기준), 람다 활용
# books = [{
#     "제목": "혼자 공부하는 파이썬",
#     "가격": 18000
# }, {
#     "제목": "혼자 공부하는 머신러닝 + 딥러닝",
#     "가격": 26000
# }, {
#     "제목": "혼자 공부하는 자바스크립트",
#     "가격": 24000
# }]
# 순차정렬 (오름차순)
# books.sort(key=lambda book: book["가격"])
# for book in books:
#     print(book)
# 역순정렬 (내림차순)
# books.sort(reverse=True, key=lambda book: book["가격"])
# for book in books:
#     print(book)

# ======================================
# p342 ----- 05-3 함수 고급 - 좀더알아보기 : 스택, 힙  -----
# ======================================
# 스택 stack : 기본자료형 보관공간
# ex) a=10, b=True, c="안녕하세요"  => 스택: 아래서부터 위로 쌓임
# 힙 heap : 객체자료형 보관공간 / 리스트,딕셔너리 주소값(자료위치or레퍼런스) -> 스택에 기록(0x... 16진수표현)

# ======================================
# p345 ----- 05-3 함수 고급 - 좀더알아보기 : 함수의 값 복사와 레퍼런스 복사  -----
# ======================================
# 전역스택 global stack: 가장 외곽에 있는 스택, 함수스택
# 예제1 -- 기본자료형 복사
# def primitive_change(b):
#     b=20
# a=10
# print(a)
# primitive_change(a)
# print(a)
# 예제2 -- 객체자료형 복사
# def object_change(d):
#     d.append(4)
# c = [1,2,3]
# print(c)
# object_change(c)
# print(c)
# 예제3 -- 객체자료형 복사
# def object_change2(f):
#     f = [4,5,6]  # → 새 리스트에 재할당 (원본 영향 X)
#     # f[0] = 4   # → 리스트 내부 값 변경 (원본 영향 O)
#     # f[1] = 5
#     # f[2] = 6
# e = [1,2,3]
# print(e)
# object_change2(e)
# print(e)

# ======================================
# p350 ----- 05-3 함수 고급 - 좀더알아보기 : global 키워드  -----
# ======================================
# 읽기 + 객체 내부 수정 → global 필요 없음.
# 재할당 (a = ... ) → global 필요함.      # UnboundLocalError 에러 발생 (global 추가 안할경우)
# 예제1 -- 객체 내부 수정
# a = [1,2,3]
# def func():
#     print(a)
#     a.append(4)
#     print(a)
# func()
# 예제2 -- 재할당
# a = 10
# def func():
#     # global a
#     print(a)
#     a = 20
#     # print(a)
# func()
# 예제3 -- 재할당(리스트)
# a = [1,2,3]
# def func():
#     # global a
#     print(a)
#     a = [4,5,6]
#     # print(a)
# func()

# ======================================
# p352 ----- 05-3 함수 고급 - 문제풀이  -----
# ======================================
# 문제1 -- 
# numbers = [1,2,3,4,5,6]
# print("::".join(map(str,numbers)))
# 문제2 -- 
# numbers = list(range(1, 10+1))
# print("# 홀수만 추출하기")
# print(list(filter(lambda x: x%2 != 0, numbers)))
# print("# 3이상, 7미만 추출하기")
# print(list(filter(lambda x: 3 <= x < 7, numbers)))
# print("# 제곱해서 50미만 추출하기")
# print(list(filter(lambda x: x**2 < 50 , numbers)))
# 도전문제1 -- 하노이탑 : 원판 개수가 n개일 때 어떻게 원판을 옮겨야 하는지 출력하도록 프로그램을 구현하시오.
# def hanoi(disk, start, result, assistance):
#     if disk == 1:
#         print(start, "→", result)
#     else:
#         hanoi(disk-1, start, assistance, result)
#         print(start, "→", result)
#         hanoi(disk-1, assistance, result, start)
# n = int(input("원판의 개수를 입력해주세요: "))
# hanoi(n, "A탑", "B탑", "C탑")

# 도전문제2 -- 하노이탑 : 원판 이동 횟수 구하시오.
# count = 0
# def hanoi(disk, start, result, assistance):
#     global count
#     if disk == 1:
#         count += 1
#     else:
#         hanoi(disk-1, start, assistance, result)
#         count += 1
#         hanoi(disk-1, assistance, result, start)
# n = int(input("원판의 개수를 입력해주세요: "))
# hanoi(n, "A탑", "B탑", "C탑")
# print(f"이동 횟수는 {count}회입니다.")

# 위 방법 시간 오래 걸림 => 원판개수 n개일 때 (2**n)-1 움직여야 원판 모두 옮길 수 있음
# def hanoi_move(n):
#     return (2**n)-1
# n = int(input("원판의 개수를 입력하세요.>>"))
# print(f"이동 횟수는 {hanoi_move(n)}회입니다.")

