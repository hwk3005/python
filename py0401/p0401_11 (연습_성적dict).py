# 연습_1
students=[]
count=1
title=['번호','이름','국어','영어','수학','합계','평균','등수']

print(" "*5, "[ 학생성적 프로그램 ]")
print("-"*30)
print("1. 학생성적 입력")
print("2. 학생성적 출력")
print("0. 프로그램 종료")
print("-"*30)
choice=int(input("원하는 번호를 입력하세요.>> "))

# 입력번호 확인
if choice==1:
    while True:
        print("[ 학생성적 입력 ]")
        no=count
        name=input(f"{no}번 학생이름을 입력하세요. (0.이전화면 이동)>>")
        if name=='0': break
        count+=1  # 입력 학생번호 증가
        kor=int(input("국어점수를 입력하세요.>> "))
        eng=int(input("영어점수를 입력하세요.>> "))
        math=int(input("수학점수를 입력하세요.>> "))
        total=kor+eng+math
        avg=total/3  # 평균
        rank=0  # 등수
        students.append(
            {"no":no,"name":name,"kor":kor,"eng":eng,"math":math,
             "total":total,"avg":avg,"rank":rank})
        print(f"{name} 학생성적이 등록되었습니다.")
        print()
        
elif choice==2:
    pass
else:
    pass