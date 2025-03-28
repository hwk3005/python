# 파이썬 변수타입 (*에러: 다른 타입끼리 계산할 경우, 숫자가 아닌 것을 숫자로 변환하려고 하는 경우 등)
#   bool 타입: True, False
#   숫자 타입: int(정수) / float(실수)
#   str 타입: 문자열

# 변수 선언
# 변수 = 10
# a = 20
# num = 30

# 출력 print()
a=10
print("안녕")
print("입력된 숫자:",a)  # ★
print("입력된 숫자: %d" % (a))
print("입력된 숫자: {}".format(a))  # ★★ 
print(f"입력된 숫자: {a}")  # ★★

# 입력 input() (str타입)
# 입력된 값은 str타입이기 때문에 => 형변환을 해줘야 함.
num1=int(input("숫자를 입력하세요."))  # 문자열 → 숫자(정수)  (ex. 안 바꿨을 때 +하면 => 100200)
num2=int(input("숫자를 입력하세요."))
print("입력된 숫자: {},{} / 합계: {}".format(num1,num2,num1+num2))  # .과 format 붙이기 (띄어쓰기x)


# Q. 학생성적 프로그램
#  이름, 국어,영어,수학 입력받아, 합계,평균을 출력하는 프로그램을 구현
print("-"*50)
print("학생성적프로그램")
print("-"*50)
name=input("이름을 입력하세요.>> ") #str타입
kor=int(input("국어점수를 입력하세요.>> ")) #str → int
eng=int(input("영어점수를 입력하세요.>> "))
math=int(input("수학점수를 입력하세요.>> "))
total=kor+eng+math
avg=(kor+eng+math)/3
print()
print("이름\t국어\t영어\t수학\t합계\t평균")
print("-"*50)
print("{}\t{}\t{}\t{}\t{}\t{:.2f}".format(name,kor,eng,math,total,avg))


