
# fifo / lifo (last in first out)
# ----------------------------------------------
# zip: 2개 리스트를 합치는 것 → list / dict타입 변경 가능
# zip만으로는 출력 안 됨 → list, dict 같이 써야 됨 
n_list=['홍길동','유관순','이순신','강감찬','김구']
t_list=[100,99,89,79,100]
print(list(zip(n_list,t_list)))  # 2개 이상 리스트 합침 가능
print(dict(zip(n_list,t_list)))  # 2개까지만 가능

# tuple_list=list(zip(n_list,t_list))

# # ----------------------------------------------
# students={"no":1,"name":"홍길동","kor":100}
# for key,value in students.items():
#     print(f"{key}: {value}")

# # for key,value in enumerate(students):  # 0: no, 1: name, 2: kor
# #     print(f"{key}: {value}")

# # ----------------------------------------------
# # 2개의 리스트를 출력할 수 있음.
# n_list=['홍길동','유관순','이순신','강감찬','김구']
# t_list=[100,99,89,79,100]
# for n,t in zip(n_list,t_list):
#     print(f"{n}: {t}")

# # ----------------------------------------------
# # 리스트 내포: if조건절을 넣을 수 있음.
# n_list=[i for i in range(1,51) if i%2==1]  # i%3==0 3의 배수 구할 때
# print(n_list)

# # ----------------------------------------------
# list=[1,2,3,4,5]
# # list +100, *100, 천단위표시 
# # format함수 천단위 표시
# list2=["{:,d}".format((i+100)*100) for i in list]
# print(list2)

# # list2=[i+100 for i in list]  # 리스트내포  # list2=[101,102,103,104,105]
# # list2=[i for i in list]  # ['10,100','10,200','10,300','10,400','10,500']

# # ----------------------------------------------
# # dict set → 중복을 제거해서 키를 확인
# myset1= {1,2,2,3,3,3,5,5,7}
# print(myset1)  # 2개 이상의 데이터 합칠 때 중복값 지울 때 등 쓰임

# menu_list=['삼각김밥','바나나','삼각김밥','사과','바나나','도시락','삼각김밥']
# print(set(menu_list))  # list타입을 set타입으로 변경해서 확인

