# ---------------------------
# 화면출력 함수선언
# ---------------------------
def stu_print():
    print("-"*40)
    print(" "*8,"[ 학생성적 프로그램 ]")
    print("-"*40)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 등수처리")
    print("5. 학생성적정렬")
    print("6. 학생성적삭제")
    print("7. 학생성적저장")  #파일저장
    print("0. 프로그램 종료")
    print("-"*40)
    choice=int(input("원하는 번호를 입력하세요.>> "))
    return choice

# ---------------------------
# 1. 학생성적입력 함수선언
# ---------------------------
def stu_input(count,students):
    print("[ 1. 학생성적입력 ]")
    no=count
    name=input(f"{no}번 학생이름을 입력하세요.>> ")
    kor=int(input("국어점수를 입력하세요.>> "))
    eng=int(input("영어점수를 입력하세요.>> "))
    math=int(input("수학점수를 입력하세요.>> "))
    total=kor+eng+math
    avg=total/3
    rank=1
    students.append({"no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"avg":avg,"rank":rank})
    print(f"{no}번 {name} 학생 성적이 등록되었습니다.")
    print()
    count+=1
    return count

