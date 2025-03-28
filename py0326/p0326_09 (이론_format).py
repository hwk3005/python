# Q1. 이름,국어,영어,수학 성적을 입력받아 합계,평균을 출력하시오.
#   이름: 홍길동
#   합계: 300
#   평균: 100.0 소수점은 1자리까지 출력하시오.

name=input("이름을 입력하세요: ")
kor=int(input("국어 점수: "))
eng=int(input("영어 점수: "))
math=int(input("수학 점수: "))
total=kor+eng+math
avg=(kor+eng+math)/3

print("이름: ",name)
print("국어: ",kor)
print("영어: ",eng)
print("수학: ",math)
print("합계: ",kor+eng+math)
print("평균: %.1f" % avg)

# 프린트 시 \n: 엔터키, \t: tab키
# print("안녕하세요.\n 반갑습니다.\t 저는 홍길동이라고 합니다.")

# ★★★ format(),f함수 많이 쓰임
# format() 문자형태 지정 함수
a=10
b=3
print("%d/%d=%.2f" % (a,b,a/b))
str_print="{}/{}={:.2f}".format(a,b,a/b)
print(str_print)
# f함수 = format()
str_print2=f"{a}/{b}={(a/b):.2f}"
print(str_print2)


