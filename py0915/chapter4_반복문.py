# ---------------------------------
# Chapter 04 반복문


# ======================================
# ----- 리스트 list -----
# ======================================
# 요소(element): 리스트 대괄호[] 내부에 넣는 자료
# 인덱스: 대괄호[] 안에 들어간 숫자, 리스트 기호

# 예제1 -- 리스트 선언 후 요소에 접근하기
# list_a = [273,32,103,"문자열",True,False]
# print(list_a[0])
# list_a[0]="변경"
# print(list_a)
# print(list_a[-2])
# print(list_a[3][0:2])
# 예제2 -- 리스트 선언 후 요소에 접근하기
# list_b = [ [1,2,3],[4,5,6],[7,8,9] ]
# print(list_b[0][2])

# 예제3 -- IndexError 존재하지 않는 위치의 요소 꺼내려고 할 때 발생
# list_a = [273,32,103]
# print(list_a[3])  # error 발생

# 예제4 -- 리스트 연산하기: 연결(+), 반복(*), len()
# list_a = [1,2,3]
# list_b = [4,5,6]
# print(list_a + list_b)  # 리스트 연결연산자
# print(list_a * 3)       # 리스트 반복연산자
# print(len(list_a))      # 함수 (길이구하기)

# 예제5 -- 리스트에 요소 추가: append(), insert(), extend()
# list_a = [1,2,3]
# list_a.append(4)    # 리스트 뒤에 요소 추가
# list_a.append(5)
# print(list_a)
# list_a.insert(0,10) # 리스트 중간에 요소 추가 (거의 사용x)
# print(list_a)
# list_a.extend([6,7,8])  # 여러 요소 추가
# print(list_a)

### 리스트 연결연산자 vs 요소추가 차이
# + 리스트 연결연산자 (비파괴적 처리 - 원본 변경x)
# append, insert, extend 요소 추가 (파괴적 처리 - 원본 변경o)

# 예제6 -- 리스트에 요소 제거: del키워드, pop(), remove(), clear()
# 1) 요소 하나 제거
# list_a = [0,1,2,3,4,5]
# del list_a[1]
# print(list_a)
# list_a.pop(3)
# print(list_a)
# 2) 값으로 제거
# list_b = [1,2,1,2]
# list_b.remove(1)    # (앞에서부터) 1 하나 제거
# print(list_b)
# 3) 모두 제거
# list_d = [0,1,2,3,4,5]
# list_d.clear()
# print(list_d)

# 예제7 -- 리스트 정렬: sort() 순차, sort(reverse=True) 역순
# list_e = [52,273,103,32,275,1,7]
# list_e.sort()
# print(list_e)
# list_e.sort(reverse=True)
# print(list_e)

# 예제8 -- 리스트 내부에 있는지 확인: in/not in 연산자
# list_a = [273,32,103,57,52]
# print(273 in list_a)
# print(99 in list_a)
# print(103 not in list_a)

# ======================================
# ----- for 반복문 -----
# ======================================
# p207 -- 예제1 -- 기본
# for i in range(5): print("출력")
# 예제2 -- for반복문과 리스트
# array = [273,32,103,57,52]
# for i in array: print(i)
# 예제3 -- for반복문과 문자열
# for i in "12345": print("-",i)

# 예제4 -- 중첩리스트, 중첩반복문
# list_of_list = [
#     [1,2,3],
#     [4,5,6,7],
#     [8,9] ]
# for i in list_of_list:
#     for j in i:
#         print(i)

# p212 -- 예제5 -- 전개연산자
# 1) 리스트 내부에 사용하는 경우
# a = [1,2,3,4]
# b = [*a, *a]
# print(b)
# a.append(5)   # 내용 변경됨
# print(a)
# b = [1,2,3,4]
# c = [*b, 5]   # 새로운 리스트 c 만들어짐
# print(b)
# print(c)
# 2) 함수 매개변수 위치에 사용하는 경우
# a = [1,2,3,4]
# print(*a)

# ======================================
# p216 ----- 딕셔너리와 반복문 -----
# ======================================
# 자료형    의미                    가리키는 위치   선언 형식   사용예           틀린예           에러발생
# 리스트    인덱스 기반으로 값 저장     인덱스        변수=[]    list_a[1]                       IndexError
# 딕셔너리  키 기반으로 값 저장         키           변수={}    dict_a["name"]  dict_a{"name"}  KeyError

# p217 -- 예제1 -- 딕셔너리 선언하기
# dict_a = {
#     "key": "value",
#     "name": "어벤져스",
#     "type": "히어로 무비"}
# # p217 -- 예제2 -- 딕셔너리 요소에 접근하기
# print(dict_a["name"])
# print(dict_a["type"])
# dict_b = {
#     "director": ["안소니 루소","조 루소"],
#     "cast": ["아이언맨","타노스","토르"]
# }
# print(dict_b["cast"])
# p219 -- 예제3 -- 딕셔너리 요소에 접근하기
# dictionary = {
#     "name": "7D 건조 망고",
#     "type": "당절임",
#     "ingredient": ["망고","설탕","치자황색소"],
#     "origin": "필리핀"
# }
# print("name:",dictionary["name"])
# print("ingredient:",dictionary["ingredient"])
# dictionary["name"] = "8D 건조 망고"  # 값변경
# print("name:",dictionary["name"])
# p220 -- NameError - key에도 큰따옴표 꼭 붙이기
# dict = {
#     name: "7D 건조망고"
# }

# p222 -- 예제4 -- 딕셔너리에 값 추가하기
# dictionary = {}
# print("요소 추가 전:",dictionary)
# dictionary["name"] = "새로운 이름"
# dictionary["body"] = "새로운 몸"
# print("요소 추가 후:",dictionary)

# p223 -- 예제5 -- 딕셔너리에 값 제거하기
# dictionary = {
#     "name": "7D 건조 망고",
#     "type": "당절임" }
# print("요소 제거 전:",dictionary)
# del dictionary["name"]
# del dictionary["type"]
# print("요소 제거 후:",dictionary)
# KeyError : 존재하지 않는 키에 접근시 error 발생

# p224 -- 예제6 -- in키워드: 딕셔너리 내부에 키 있는지 확인
# dictionary = {
#     "name": "7D 건조 망고",
#     "type": "당절임" }
# key = input("접근하고자 하는 키: ")
# if key in dictionary: print(dictionary[key])
# else: print("존재하지 않는 키에 접근하고 있습니다.")

# p225 -- 예제7 -- get() 함수 : 딕셔너리 내부에 키 있는지 확인 - KeyError 발생대신 None 출력해줌
# dictionary = {
#     "name": "7D 건조 망고",
#     "type": "당절임" }
# value = dictionary.get("존재하지 않는 키")
# value2 = dictionary.get("name")
# print("값:",value)
# print("값:",value2)

# p226 -- 예제8 -- for반복문과 딕셔너리
# dictionary = {
#     "name": "7D 건조 망고",
#     "type": "당절임" }
# for key in dictionary:
#     print(key,":",dictionary[key])

# ======================================
# 범위자료형 - 특정한 횟수만큼 반복해서 돌리고 싶을 때 for문과 범위 조합해서 사용함
# ======================================
# p231 -- 예제1
# print(list(range(0,5,2)))
# print(list(range(0,10,3)))
# a = range(0,10+1)
# print(list(a))
# p233 -- 예제2 -- TypeError
# n=10
# a = range(0,int(n/2))
# b = range(0, n//2)
# print(list(a))
# print(list(b))

# p234 -- 예제3 -- for반복문-범위와 함께 사용하기
# for i in range(5):
#     print(str(i) + "= 반복변수")
# print()
# for i in range(0,10,3):
#     print(str(i) + "= 반복변수")

# p235 -- 예제4 -- for반복문-리스트와 범위 조합하기
# array = [273,32,103,57,52]
# for i in range(len(array)):
#     print("{}번째 반복: {}".format(i,array[i]))

# p235 -- 예제5 -- for반복문-역반복문 (반대로 반복하기)
# for i in range(4,0-1,-1):
#     print("현재 반복 변수: {}".format(i))
# for i in reversed(range(5)):
#     print("현재 반복 변수: {}".format(i))

# p237 -- 예제6 -- 중첩반복문으로 피라미드 만들기
# output = ""
# for i in range(1,5+1):
#     for j in range(0,i):
#         output += "*"
#     output += "\n"
# print(output)
# p239 -- 예제7 -- 중첩반복문으로 피라미드 만들기2
# output = ""
# for i in range(1,15):
#     for j in range(14,i,-1):
#         output += " "
#     for k in range(0,2*i-1):
#         output += "*"
#     output += "\n"
# print(output)
# p240 -- 예제8 -- 문자열 *연산자로 피라미드 만들기
# output = ""
# for i in range(1,10):
#     output += ("*" * i)
#     output += "\n"
# print(output)

# ======================================
# p240 ----- while 반복문 -----
# ======================================
# p240 -- 예제1 -- 무한반복
# while True:
#     print(".", end="")
# 예제2 -- while반복문: for반복문처럼 사용하기
# i=0
# while i < 10:
#     print("{}번째 반복입니다.".format(i))
#     i+=1
# 예제3 -- 상태 기반으로 반복 : 해당하는 값 모두 제거하기
# list_test = [1,2,1,2]
# value = 2
# while value in list_test:
#     list_test.remove(value)
# print(list_test)

# 유닉스타임 UTC (세계표준시)
# import time
# print(time.time())
# 예제4 -- 시간 기반으로 반복 : 5초 동안 반복하기
# import time
# number = 0
# target_tick = time.time()+5
# while time.time() < target_tick:
#     number+=1
# print(f"5초 동안 {number}번 반복했습니다.")
# 예제5 -- break 키워드
# i=0
# while True:
#     print(f"{i}번째 반복문입니다.")
#     i+=1
#     input_text=input("종료하시겠습니까?(y/n)>>")
#     if input_text in ["y","Y"]:
#         print("반복을 종료합니다.")
#         break
# 예제6 -- continue 키워드
# numbers = [5,15,6,20,7,25]
# for number in numbers:
#     if number < 10:     # 10보다 작으면 반복대상에서 제외
#         continue
#     print(number)

# ======================================
# p250 -- 문자열, 리스트, 딕셔너리 관련 기본함수 --  min(),max(),sum(), reversed(), enumerate()-list, items()-dict, 리스트 내포
# ======================================
# 예제1 -- 리스트에 적용할 수 있는 기본함수: min()최솟값, max()최댓값, sum()합
# numbers = [103,52,273,32,77]
# print("최소값:",min(numbers))
# print("최대값:",max(numbers))
# print("총합계:",sum(numbers))

# 예제2 -- 리스트 뒤집기 (역순정렬) : reversed() 함수 - 결과 제너레이터
# 1) 
# list_a = [1,2,3,4,5]
# list_reversed = reversed(list_a)
# print("reversed([1,2,3,4,5]):",list_reversed)
# print("list(reversed([1,2,3,4,5])):",list(list_reversed))
# print("for i in reversed([1,2,3,4,5]):")
# for i in reversed(list_a):
#     print("-",i)
# print(list(reversed(list_a)))
# 2) 안 쓰는 예
# temp = reversed([1,2,3,4,5,6])
# for i in temp:
#     print(f"첫 번째 반복문: {i}")
# for i in temp:
#     print(f"두 번째 반복문: {i}")
# 3) 수정본
# numbers = [1,2,3,4,5,6]
# for i in reversed(numbers):
#     print("첫번째 반복문: {}".format(i))
# for i in reversed(numbers):
#     print("두번째 반복문: {}".format(i))

# 예제3 -- enumerate() 함수와 반복문 조합하기  # enumerate 사용시 반복변수 2개 넣기 가능 (ex. for i,n in numbers)
# example_list = ["요소A","요소B","요소C"]
# # 1) 방법1 - enumerate() 함수 사용x
# i=0
# for item in example_list:
#     print(f"{i}번째 요소는 {item}입니다.")
#     i+=1
# # 2) 방법2 - enumerate() 함수 사용x
# for i in range(len(example_list)):
#     print(f"{i}번째 요소는 {example_list[i]}입니다.")
# 3) enumerate() 함수 사용o
# print("단순출력:",example_list)
# print("enumerate사용:",enumerate(example_list))  # 주소값 출력됨
# print("list함수로 강제변환후 출력:",list(enumerate(example_list)))
# print("for문과 enumerate함수 조합")
# for i, value in enumerate(example_list):      # enumerate 사용시 반복변수 2개 넣기 가능
#     print(f"{i}번째 요소는 {value}입니다.")

# 예제4 -- 딕셔너리 items()함수 & 반복문
# example_dictionary = {
#     "키A":"값A",
#     "키B":"값B",
#     "키C":"값C"
# }
# print("items():",example_dictionary.items())
# for key, element in example_dictionary.items():
#     print("dictionary[{}] = {}".format(key,element))

# p257 -- 예제5 -- 리스트내포 : 반복문 사용한 리스트 생성
# array = []
# for i in range(0,20,2):
#     array.append(i*i)
# print(array)  # [0, 4, 16, 36, 64, 100, 144, 196, 256, 324] (0*0, 2*2, 4*4, 6*6, 8*8, ...)
# 예제6 -- 리스트내포 : 리스트 안에 for문 사용하기
# array = [i*i for i in range(0,20,2)]
# print(array)

# 리스트내포 list comprehensions
# 리스트이름 = [표현식 for 반복자 in 반복할 수 있는 것 (if 조건문) ]

# 예제6 -- 리스트내포 : 조건을 활용한 리스트내포
# array = ["사과","자두","초콜릿","바나나","체리"]
# output = [fruit for fruit in array if fruit != "초콜릿"]
# print(output)

# ======================================
# p260 -- 구문 내부에 여러 줄 문자열 사용했을 때 문제점 - 해결방법: 괄호로 문자열 연결, 문자열 join()함수 사용
# ======================================
# 예제1 -- 문제
# number = int(input("정수입력>> "))
# if number%2 == 0:
#     print("""\
#         입력한 문자열은 {}입니다.
#         {}는(은) 짝수입니다.""".format(number,number))
# else:
#     print("""\
#         입력한 문자열은 {}입니다.
#         {}는(은) 홀수입니다.""".format(number,number))

# 예제2 -- 해결방법1 : 괄호로 문자열 연결하기
# 1) 예시
# test = {
#     "이렇게 입력해도 "
#     "하나의 문자열로 연결되어 "
#     "생성됩니다."
# }
# print("test:",test)
# print("type(test):",type(test))
# 2) 위 문제 괄호로 해결
# number = int(input("정수입력>> "))
# if number%2 == 0:
#     print( (
#         "입력한 문자열은 {}입니다.\n"
#         "{}는(은) 짝수입니다."
#     ).format(number,number) )
# else:
#     print( (
#         "입력한 문자열은 {}입니다.\n"
#         "{}는(은) 홀수입니다."
#     ).format(number,number) )

# 예제3 -- 해결방법2 : 문자열 join() 함수: 리스트 요소를 문자열로 연결 => 문자열.join(문자열로 구성된 리스트)
# 1) 예시
# print("::".join(["1","2","3","4","5"]))
# 2) 위 문제 join()함수로 해결
# number = int(input("정수입력>>"))
# if number%2 == 0:
#     print("\n".join([
#         "입력한 문자열은 {}입니다.",
#         "{}는(은) 짝수입니다."
#     ]).format(number,number) )
# else:
#     print("\n".join([
#         "입력한 문자열은 {}입니다.",
#         "{}는(은) 홀수입니다."
#     ]).format(number,number) )

# ======================================
# p264 -- 이터레이터iterator : 이터러블 중 next()함수 적용해 하나하나 꺼낼 수 있는 요소
# ======================================
# for 반복자 in 이터러블iterable(반복할 수 있는 것)
# 예제1 -- reversed() 함수와 이터레이터
# numbers = [1,2,3,4,5,6]
# r_num = reversed(numbers)
# print("reversed_numbers:",r_num)
# print(next(r_num))
# print(next(r_num))
# print(next(r_num))
# print(next(r_num))
# for i in reversed(numbers):
#     print(i)

# reversed() 역순정렬
# enumerate() 매개변수에 리스트 넣으면 인덱스, 값 쌍으로 사용해 반복문 돌릴 수 있게 해주는 함수
# items() 키와 쌍으로 사용해 반복문 돌릴 수 있게 해주는 딕셔너리 함수
# 리스트내포 반복문, 조건문을 대괄호[] 안에 넣어 리스트 생성하는 파이썬의 특수한 구문

# 4장 도전문제
# (문제1)
# list = [1,2,3,4,1,2,3,1,4,1,2,3]
# counter = {}
# for i in list:
#     if i not in counter:
#         counter[i] = 0
#     counter[i] += 1
# print( (f"{list}에서\n"
#         f"사용된 숫자의 종류는 {len(counter)}개입니다.") )
# (문제2)
# nucleos = input("염기 서열을 입력해주세요(a,t,g,c)>> ")
# counter = {
#     "a":0,
#     "t":0,
#     "g":0,
#     "c":0
# }
# for nucleo in nucleos:
#     counter[nucleo]+=1
# for key in counter:
#     print(f"{key}의 개수: {counter[key]}")
# (문제3)
# nucleos = input("염기 서열을 입력해주세요(a,t,g,c)>> ")
# counter = {}
# for i in range(0, len(nucleos),3):
#     codon = nucleos[i:i+3]  # 3글자씩 추출
#     if len(codon) == 3:
#         if codon not in counter:
#             counter[codon]=0
#         counter[codon]+=1
# print(counter)
# (문제4)   - 정답: p537
# a = [1,2,[3,4],5,[6,7],[8,9]]
# output = []  # 최종적으로 평탄화된 결과를 넣을 빈 리스트 준비
# for i in a:  # a의 요소 하나씩 꺼내옴 / i : 1, 2, [3,4], 5, [6,7], [8,9]
#     if type(i) == list:
#         for j in i:  # i의 리스트요소 하나씩 꺼냄 / ex) i = [3,4]라면 j는 3, 4
#             output.append(j)
#     else:
#         output.append(i)
# print( (f"{a}를 평탄화하면\n"
#         f"{output}입니다.") )
