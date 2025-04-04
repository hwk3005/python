# lambda, map, filter, sort, sorted

students = [
    {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
    {"no":2,"name":"유관순","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
    {"no":3,"name":"이순신","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
]


# sorted 기존의 리스트는 유지, 새로운 리스트 생성 (※메모리 차지 많이 함.)
s_list=sorted(students,key=lambda x:x['name'])
print(s_list)
print("-"*60)
print(students)

# # sort() 기존의 리스트의 값을 변경시킴.
# # 합계 정렬방법 ---------
# print(students)
# print("-"*60)
# students.sort(key=lambda x:x['total'])  # 합계 순차정렬
# print(students)
# print("-"*60)
# students.sort(key=lambda x:x['total'],reverse=True)  # 합계 역순정렬
# print(students)
# # 이름 정렬방법 ---------
# students.sort(key=lambda x:x['name'])  # 이름으로 순차정렬
# print(students)
# print("-"*60)
# students.sort(key=lambda x:x['name'],reverse=True)  # 이름으로 역순정렬
# print(students)
# #_______________________________________
# # dict타입 sort() 함수 사용할 수 없음. (lambda 함수로는 가능)
# students.sort()
# print(students)  # 정렬할 수 없는 형식이라고 에러남.
# #--------------
# # list타입 sort() 정렬됨
# a_list=[20,50,10,40,90]
# a_list.sort()              # 순차정렬
# print(a_list)
# a_list.sort(reverse=True)  # 역순정렬
# print(a_list)
# #_______________________________________
# 람다식 lamda → 함수 축약형
# def 함수명(매개변수) : return 값
# lambda 매개변수 : return값
# lambda a:a*20
# #--------------------------------
# map() 함수: 리스트에 함수를 적용한 결과를 다시 리스트(iterator)로 반환
# filter() 함수: 리스트에 함수를 적용해서 조건에 맞는 것(True)만 다시 리스트로 반환

# #_______________________________________

# # filter() 함수 관련
# a_list=[1,2,3,4,5]
# aa_list=[]
# for i in a_list:
#     if i%2==0:
#         aa_list.append(i)
# print(aa_list)
# # filter() 함수 사용
# def func(x):
#     if x%2==0:
#         return x

# b_list=list(filter(func,a_list))
# print(b_list)
# # lambda 함수 사용
# c_list=list(filter(lambda x:x%2==0,a_list))
# print(c_list)
# #_______________________________________
# ## map
# a_list=[1,2,3,4,5]  # list 모든 값에 제곱을 해서 리스트를 생성
# aa_list=[]
# for i in a_list:
#     aa_list.append(i**2)
    
# # ▼ 위와 동일한 방법
# # map(함수,리스트): 리스트에 있는 내용에 함수를 적용한 결과를 다시 iterator(리스트)로 변환시켜줌.
# def func(x):
#     return x**2  # 이 형식을 아래 func에 넣은 것, lambda 사용시 1줄로 줄일 수 있음.
# print(list(map(func,a_list)))

# # 람다식 - map() 함수를 lambda로 사용하면 코드를 줄일 수 있음.
# print(list(map(lambda x:x**2,a_list)))

# #_______________________________________
# def add(a,b):
#     return a+b
# print(add(10,20))

# def func(a,b,c):
#     return max(a,b,c)
# print(max(10,5,20))
