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


