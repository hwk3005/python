### 학생성적 프로그램
### 진행하세요. ~~~ 시험  / 입력 출력 수정 삭제 정렬 검색 종료

from stuFunc import *

students=[
    {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100,"rank":1},
    {"no":2,"name":"유관순","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
    {"no":3,"name":"이순신","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2}
]
count=4
title=['번호','이름','국어','영어','수학','합계','평균','등수']
choice=0


    
while True:
    ## 화면출력 부분
    choice=stu_print()
    
    if choice==1:   # 1. 학생성적 입력부분
        count=stu_input(count,students)
    
    if choice==2:   # 2. 학생성적 출력부분
        print(" "*20,"[ 2. 학생성적출력 ]")
        print("-"*60)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print("-"*60)
        for s in students:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
        print()
    
    if choice==3:   # 3. 학생성적 수정부분
        print("[ 3. 학생성적수정 ]")
        temp=0  # 찾지 못했을 경우
        name=input("수정하려고 하는 학생이름을 입력하세요.>> ") # input
        for s in students:
            if s['name']==name:
                temp=1  # 찾았을 경우
                print(f"{name} 학생을 찾았습니다. 성적을 수정합니다.")
                print("[ 수정과목 선택 ]")
                print("1. 국어")
                print("2. 영어")
                print("3. 수학")
                print("-"*10)
                choice=int(input("수정할 과목 번호를 입력하세요.>> "))
                sub_list=['','kor','eng','math']
                if choice ==1:
                    pre_score=s[sub_list[choice]]
                    print(f"현재 {title[choice+1]}점수: {pre_score}")
                    s[sub_list[choice]]=int(input(f"수정할 {title[choice+1]}점수 입력: "))
                    print(f"변경 전 {pre_score}점이 {s[sub_list[choice]]}점으로 수정되었습니다.")
                    s['total']=s['kor']+s['eng']+s['math']
                    s['avg']=s['total']/3
                elif choice==2:
                    pre_score=s[sub_list[choice]]
                    print(f"현재 {title[choice+1]}점수: {pre_score}")
                    s[sub_list[choice]]=int(input(f"수정할 {title[choice+1]}점수 입력: "))
                    print(f"변경 전 {pre_score}점이 {s[sub_list[choice]]}점으로 수정되었습니다.")
                    s['total']=s['kor']+s['eng']+s['math']
                    s['avg']=s['total']/3
                elif choice==3:
                    pre_score=s[sub_list[choice]]
                    print(f"현재 {title[choice+1]}점수: {pre_score}")
                    s[sub_list[choice]]=int(input(f"수정할 {title[choice+1]}점수 입력: "))
                    print(f"변경 전 {pre_score}점이 {s[sub_list[choice]]}점으로 수정되었습니다.")
                    s['total']=s['kor']+s['eng']+s['math']
                    s['avg']=s['total']/3
                # if 1<= choice <=3:
                #     pre_score=s[sub_list[choice]]
                #     print(f"현재 {title[choice+1]}점수: {pre_score}")
                #     s[sub_list[choice]]=int(input(f"수정할 {title[choice+1]}점수 입력: "))
                #     print(f"변경 전 {pre_score}점이 {s[sub_list[choice]]}점으로 수정되었습니다.")
                    
                #     s['total']=s['kor']+s['eng']+s['math']
                #     s['avg']=s['total']/3
                else: print("잘못된 번호입니다. 번호를 다시 입력하세요.")
        if temp==0:
            print(f"{name} 학생을 찾지 못했습니다. 다시 입력하세요.")
            print()
    
    if choice==4:   # 4. 등수처리
        print("[ 4. 등수처리 ]")
        for s in students:
            num=1
            for ss in students:
                if s['total'] < ss['total']:    # 등수비교
                    num+=1                      # 등수 1증가
            s['rank']=num                       # 등수적용
        print("등수처리가 완료되었습니다.")
        print()
        
    if choice==5:   # 5. 학생성적정렬
        students2=[*students]  # 복사
        print("[ 5. 학생성적정렬 ]")
        print("1. 이름 순차정렬")
        print("2. 이름 역순정렬")
        print("3. 합계 순차정렬")
        print("4. 합계 역순정렬")
        print("5. 번호 순차정렬")
        print("6. 번호 역순정렬")
        print("0. 이전화면이동")
        print("-"*30)
        choice=int(input("원하는 번호를 입력하세요.>> "))
        if choice==1:   # 이름 순차정렬
            students2.sort(key=lambda x:x['name'])
        elif choice==2:   # 이름 역순정렬
            students2.sort(key=lambda x:x['name'],reverse=True)
        elif choice==3:   # 합계 순차정렬
            students2.sort(key=lambda x:x['total'])
        elif choice==4:   # 합계 역순정렬
            students2.sort(key=lambda x: x['total'],reverse=True)
        elif choice==5:   # 번호 순차정렬
            students2.sort(key=lambda x: x['no'])
        elif choice==6:   # 번호 역순정렬
            students2.sort(key=lambda x: x['no'],reverse=True)
        elif choice==0:   # 이전화면이동
            continue
        print(title,students2)
        
        
    if choice==0:   # 0. 프로그램 종료
        print("[ 프로그램 종료 ]")
        break

    
    

