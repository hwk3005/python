# 일반변수: bool, str, int, float (지역변수와 전역변수값 다름(전역변수값 호출됨 → return사용))
# 그룹변수: list, dict,           (지역변수와 전역변수값 동일)
# - 지역변수: 함수 내에 선언되어 있는 변수 (함수 벗어나면 완전 사라짐)
# - 전역변수: 함수 외에 선언되어 있는 변수
# return()  (호출하는 대로) 값을 돌려줌.
# ________________________________________________________________




# def cal(*a,b=10):  # 가변매개변수, 키워드매개변수 함께 사용 - 매개변수 키워드
#     result=b
#     for i in a:
#         result+=i
#     return result

# print(cal(1,2,b=100))  # b=100 키워드매개변수


# # ---------------
# def cal(b=10,*a):
#     result=b
#     for i in a:
#         result+=i
#     return result

# print(cal(1,2,3,4,5))  # 1은 b에, 2,3,4,5는 a에 값 들어감
# _____________________
# # 키워드 매개변수 (키워드변수는 무조건 마지막에 있어야 함. => b=10)
# # def cal(b=10,a):
# def cal(a,b=10):
#     return a+b
# print(cal(1))
# _____________________
# # print()함수는 매개변수가 가변매개변수임.
# print(1,2,3,4,5)
# print(1,2)
# # ---------------
# # 가변매개변수 사용
# def cal (*num):  # 전개연산자 1,2,3,4,5
#     result=0
#     for n in num:
#         result+=n
#     return result

# print("2개 합계: ",cal(1,2))
# print("3개 합계: ",cal(10,20,30))
# print("4개 합계: ",cal(20,40,60,80))
# # ---------------
# def cal(n1,n2):
#     return n1+n2
# def cal2(n1,n2,n3):
#     return n1+n2+n3
# def cal3(n1,n2,n3,n4):
#     return n1+n2+n3+n4

# n1=10
# n2=20
# n3=30
# n4=40
# result=cal(n1,n2)
# print(result)

# result2=cal2(n1,n2,n3)
# print(result2)
# _____________________
# # global 변수: 전역변수  (파이썬에만 있음)
# def func1():
#     global a  # 전역변수 호출
#     a=20
#     # a=20  # 지역변수이기에 함수를 벗어나면 사라짐.
# a=10
# print("a: ",a)  # a: 10
# func1()
# print("a: ",a)  # a: 10
# _____________________
# ## 함수 선언 부분 ##
# def func1():
#     a=10 # 지역변수
#     print("func1()에서 a값 %d"%a)
# ## 전역 변수 선언 부분 ##
# a=20
# ## 메인 코드 부분 ##
# func1()  # => 전역변수값 가져옴
# _____________________
# 함수 선언
# def cal(ss):
#     ss['kor']=int(input("수정할 국어점수를 입력하세요.>> "))
#     ss['total']=ss['kor']+ss['eng']+ss['math']
#     ss['avg']=ss['total']/3

# print("[ 학생성적 수정 ]")
# s={"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1}
# # 국어점수변경 함수호출
# cal(s)  # 변경된 국어점수 입력됨.
# print("수정된 국어점수: ",s['kor'])
# ---------------
# # 일반변수 → 매개변수로 전달형태 (리턴으로 값을 돌려줘서 입력을 시켜야 함.)
# # 국어점수변경 함수선언
# def cal(kor):
#     kor=int(input("수정할 국어점수를 입력하세요.>> "))
#     return kor  # 일반변수 경우에 return을 해줘야 반영됨

# print("[ 학생성적 수정 ]")
# kor=100
# eng=100
# math=100
# # 국어점수변경 함수호출
# kor=cal(kor)  # 변경된 국어점수 입력됨.
# print("수정된 국어점수: ",kor)

# ---------------
# def cal(b_list):
#     b_list[0]=100
#     b_list[1]=200

# a_list=[0,0]  # 리스트타입 변수: 주소값 들어가있음.
# a_list[0]=10
# a_list[1]=20
# print("함수 호출 전 a_list: ",a_list[0],a_list[1])  # 10,20

# cal(a_list)  # 함수 호출  b_list = a_list
# print("함수 호출 후 a_list: ",a_list[0],a_list[1])  # 100,200
# _____________________
# # 함수 선언
# def cal(a,b):
#     a=100  # 지역변수 (함수 내 일반변수는 함수를 벗어나면 사라짐. - bool, str, int, float)
#     b=200
# # ----------
# # 함수밖
# a=10  # 전역변수
# b=20
# print("함수 호출 전 a,b: ",a,b)  # a=10,b=20
# # ----------
# # 함수 호출
# cal(a,b)
# print("함수 호출 후 a,b: ",a,b)  # a=10,b=20
# _____________________
# # Q5. 이름, 국어,영어,수학 점수를 입력받아, 합계,평균을 출력하시오.
# students = [
#     {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
#     {"no":2,"name":"유관순","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
#     {"no":3,"name":"이순신","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
# ]
# def stu_print():
#     for s in students:
#         print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']}\t{s['rank']}")

# print("1. 학생성적입력")
# print("2. 학생성적출력")
# choice=int(input("원하는 번호를 입력하세요.>> "))
# if choice==2:
#     stu_print()  # 함수 호출
# ----------------
# # 함수 선언
# def cal(kor,eng,math):
#     # total=kor+eng+math
#     # avg=total/3
#     return kor+eng+math, (kor+eng+math)/3
# # 입력 부분
# no=1
# name=input("이름을 입력하세요.>> ")
# kor=int(input("국어점수를 입력하세요.>> "))
# eng=int(input("영어점수를 입력하세요.>> "))
# math=int(input("수학점수를 입력하세요.>> "))
# total,avg=cal(kor,eng,math)
# print("합계: ",total,"평균: ",avg)

# _____________________
# # Q4. 직사각형 넓이와 둘레를 구하는 프로그램을 구현하시오.
# # (넓이: 가로*세로, 둘레: 가로길이*2+세로길이*2)

# # 가로, 세로길이를 입력받아 넓이와 둘레를 구하시오.
# # 함수를 사용할 것
# def cal(num1,num2):
#     result1=num1*num2
#     result2=(num1*2)+(num2*2)
#     return result1, result2

# # 가로,세로 입력
# num1=int(input("가로 길이를 입력하세요.>> "))
# num2=int(input("세로 길이를 입력하세요.>> "))
# result1,result2=cal(num1,num2)   
# print("넓이: ",result1,", 길이: ",result2)
# _____________________
# def add():
#     return 1,2
# a,b=add()
# print(a,b)
# _____________________
# # Q3. 입력을 5개를 받아, 짝수만 모두 더한 값을 출력하시오.
# def even(n):
#     if n%2==0: return n
#     else: return 0

# def cal(n_list):
#     sum=0
#     for n in n_list:
#         if n%2==0: sum+=n
#     return sum
# # ▲ cal 함수 선언하시오. ▲▲▲▲▲   
# n_list=[0]*5
# for i in range(5):
#     n_list[i]=int(input("숫자입력: "))
# result=cal(n_list)
# print("짝수의 합: ",result)
# _____________________

# # Q2. 함수를 사용해서 두 수를 입력받아
# # 10~20 입력받으면 10+11+12+13...20 출력하시오.
# # add() 결과값을 출력하시오.
# def add(n1,n2):
#     # 비교
#     if n1>n2: n1,n2=n2,n1  # 큰 수를 먼저 넣어도 10,2 → 2,10
#     sum=0
#     for i in range(n1,n2+1):
#         sum=sum+i
#     print("합계: ",sum) 

# n1=int(input("숫자를 입력하세요.>> "))
# n2=int(input("숫자를 입력하세요.>> "))
# add(n1,n2)
# _____________________
# 함수 사용
#   1. 중복코드가 있을 때
#   2. 소스가 너무 복잡할 때
#   먼저 프로그램 모두 구현해놓고, 중복되고 있는지 확인 후 함수를 사용
# _____________________
# Q1. num1,num2,num3 값을 입력받아 합계,평균을 구하시오.
# # 함수 선언
# def add(kor,eng,math):
#     return kor+eng,math

# kor=int(input('점수를 입력하세요.>> '))
# eng=int(input('점수를 입력하세요.>> '))
# math=int(input('점수를 입력하세요.>> '))
# total=add(kor+eng+math)  # 함수호출
# avg=total/3

# print(kor,eng,math,total,avg)


