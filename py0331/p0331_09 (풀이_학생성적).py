# 초기화 선언
students=list()
count=1

# 프로그램 시작
while True:
    # 화면 출력
    print("-"*30)
    print(" "*5,end="")
    print("[ 학생성적 프로그램 ]")
    print("-"*30)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 학생성적삭제")
    print("5. 학생성적정렬")
    print("6. 학생성적검색")
    print("0. 프로그램 종료")
    print("-"*30)
    
    # 번호 입력
    choice=int(input("원하는 번호를 입력하세요: "))
    print()
    
    # 원하는 프로그램 실행
    if choice == 1:
        print("[ 학생성적 입력 ]")
        no=count
        name=input("이름을 입력하세요: ")
        kor=int(input("국어점수를 입력하세요: "))
        eng=int(input("영어점수를 입력하세요: "))
        math=int(input("수학점수를 입력하세요: "))
        total=kor+eng+math
        avg=total/3
        rank=0
        student=[no,name,kor,eng,math,total,avg,rank]
        students.append(student)
        count+=1
    
    elif choice == 2:
        print("                [ 학생성적 프로그램 ]")
        print("-"*60)
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수")
        print("-"*60)
        for stu in students:
            for i,s in enumerate(stu):
                if i != 6:
                    print(s,end="\t")
                else:  # 평균일 때
                    print(f"{s:.2f}",end="\t")
            print()
        
    elif choice == 0:
        print("[ 프로그램 종료 ]")
        break
    print()
print()
    
    
    
    