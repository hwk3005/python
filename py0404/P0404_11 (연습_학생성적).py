# 파일불러오기              ◀ 1
# print(" "*10,"[ 학생성적 프로그램 ]")
# print("-"*40)
# print("1. 학생성적입력")  ◀  6
# print("2. 학생성적출력")  ◀  2
# print("3. 학생성적수정")  ◀  7
# print("4. 등수처리")      ◀  8
# print("5. 학생성적정렬")  ◀  3
# print("6. 학생성적삭제")  ◀  5
# print("7. 학생성적저장")  ◀  4
# print("0. 프로그램 종료") ◀  9
# print("-"*40)

students=[]
# 파일읽어오기
with open("py0404/stu.txt","r",encoding="utf8") as f:
    while True:
        data=f.readline()  # 1줄 읽어옴 (1,홍길동,60,100,100,260,86.66666666666667,3)
        if not data: break # '' 
        s=data.strip().split(",")  # strip() 공백제거, split(",") 분리
        students.append({
            "no":int(s[0]),"name":s[1],"kor":int(s[2]),"eng":int(s[3]),
            "math":int(s[4]),"total":int(s[5]),"avg":float(s[6]),"rank":int(s[7])
        })

count=max(students,key=lambda x:x['no'])['no']+1  # max 최대값 +1 증가
title=['번호','이름','국어','영어','수학','합계','평균','등수']

while True:
    print(" "*10,"[ 학생성적 프로그램 ]")
    print("-"*40)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("7. 학생성적저장")
    print("0. 프로그램 종료")
    print("-"*40)
    choice=int(input("원하는 번호를 입력하세요.>> "))


    if choice==1:
        print("[ 학생성적입력]")
        no=count
        name=input(f"{no}번 학생이름을 입력하세요.>> ")
        kor=int(input("국어점수를 입력하세요.>> "))
        eng=int(input("영어점수를 입력하세요.>> "))
        math=int(input("수학점수를 입력하세요.>> "))
        total=kor+eng+math
        avg=total/3
        rank=0
        # students 저장
        students.append({
            "no":no,"name":name,"kor":kor,"eng":eng,"math":math,
            "total":total,"avg":avg,"rank":rank
        })
        print(f"{no}번 {name} 학생 성적이 등록되었습니다.")
        print()
        count+=1
    
    
    elif choice==2:
        print(" "*20,"[ 학생성적출력 ]")
        print("-"*60)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print("-"*60)
        for s in students:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
        print()

    elif choice==7:
        print("[ 학생성적저장 ]")
        with open("py0404/stu.txt","w",encoding="utf8") as f:
            for s in students:
                data=f"{s['no']},{s['name']},{s['kor']},{s['eng']},{s['math']},{s['total']},{s['avg']},{s['rank']}\n"
                f.write(data)
        print("파일이 저장되었습니다.")
        print()
    
    elif choice==0:
        print("[ 프로그램 종료 ]")
        break
        
        
        
        