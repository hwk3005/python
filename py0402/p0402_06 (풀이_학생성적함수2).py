### 파일 - 저장해서 불러오기
### DB에서 불러오기


#### 전역변수 선언부분 ####
# students 리스트 타입
students = [
    {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
    {"no":2,"name":"유관순","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
    {"no":3,"name":"이순신","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
]
count = 4    # 학생번호를 생성
title = ['번호','이름','국어','영어','수학','합계','평균','등수']

### 함수 부분 ###
# 학생성적입력 함수
def stu_input(count):
    while True:
        print("[ 학생성적 입력 ]") 
        no=count
        name=input(f"{no}번 학생, 이름을 입력하세요.(0.이전화면 이동)>> ")
        # 이전화면 이동 확인
        if name=="0": break  # 학생성적입력에서 이전(전체)화면으로 이동
        score=[0]*3  # list생성
        score_cal(0,score)  # 국어점수입력, 확인
        score_cal(1,score)  # 영어점수입력, 확인
        score_cal(2,score)  # 수학점수입력, 확인
            
        # no, name, kor, eng, math
        # 합계, 평균 구하기
        total=score[0]+score[1]+score[2]
        avg=total/3
        rank=0
        # students 입력
        students.append({"no":no,"name":name,"kor":score[0],"eng":score[1],"math":score[2],"total":total,"avg":avg,"rank":rank})
        print(f"{no}번 {name} 학생 성적을 저장했습니다.")
        print()
        count+=1  # 학생수 1증가
        return count


# 국어,영어,수학점수 입력하고 확인하는 함수
def score_cal(i,score):
    while True:
        score[i]=input(f"{title[i+2]} 점수를 입력하세요.>> ")
        if score[i].isdigit():
            score[i]=int(score[i])         # 숫자변환
            if 0 <= score[i] <= 100:  # 0에서 100사이의 값인지 확인
                break
            else: print("점수는 0~100사이의 값을 입력하셔야 합니다.")
        else: print("숫자만 가능합니다.")


# 시작
while True:
    print(" "*5,end="")
    print("[ 학생성적 프로그램 ]")
    print("-"*30)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("0. 프로그램종료")
    print("-"*30)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    
    # 번호선택
    if choice == 1:
        count=stu_input(count)
                                    
    elif choice == 2:
        print(" "*20,"[ 학생성적 출력 ]")
        print("-"*60)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print("-"*60)
        for s in students:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
        print()
    elif choice==3:
        print("[ 학생성적 수정 ]")
        name=input("수정하려고 하는 학생이름을 입력하세요.(0.이전화면 이동)>> ")  # 수정하려는 이름 입력받기
        # 이전화면 이동 확인
        temp=0   # 찾고자 하는 학생이 없을 경우
        for s in students:
            if name in s['name']:  # 찾았을 경우
                temp=1             # temp = 1 변경 (찾았을 경우)
                print(f"{name} 학생이 있습니다. 성적을 수정합니다.")
                print("[ 수정할 과목 선택 ]")
                print("1. 국어")
                print("2. 영어")
                print("3. 수학")
                print("-"*10)
                choice=int(input("원하는 번호를 입력하세요.>> "))
                # 수정할 과목 확인
                if choice==1:  # 국어점수 수정
                    pre_kor=s['kor']  # 이전국어점수변수
                    print(f"현재 국어점수: {pre_kor}")
                    s['kor']=int(input("변경 국어점수: "))
                    # 합계, 평균 수정
                    s['total']=s['kor']+s['eng']+s['math']
                    s['avg']=s['total']/3
                    print(f"국어점수 {pre_kor}점이 {s['kor']} 점으로 변경되었습니다.")
                    
                elif choice==2:  # 영어점수 수정
                    pre_eng=s['eng']  # 이전영어점수변수
                    print(f"현재 영어점수: {pre_eng}")
                    s['eng']=int(input("변경 영어점수: "))
                    # 합계, 평균 수정
                    s['total']=s['kor']+s['eng']+s['math']
                    s['avg']=s['total']/3
                    print(f"영어점수 {pre_eng}점이 {s['eng']} 점으로 변경되었습니다.")
                    
                elif choice==3:
                    pre_math=s['math']
                    print(f"현재 수학점수: {pre_math}")
                    
                print()
                
        # 수정할 과목을 찾지 못했을 경우
        if temp==0:
            print("수정하고자 하는 학생을 찾지 못했습니다. 다시 입력하세요!!")
            print()

    elif choice == 0:
        print("[ 프로그램종료 ]")
        break
    
    
    
    


# dic={"no":1,"name":"홍길동"}

# if "홍길동" in dic["name"]:  # dic["name"]:
#     print("있다.")
# else: print("없다.")

# if "홍길동" in dic:
#     print("있다.")
# else: print("없다.")



            # score_cal(0,score)  # 국어점수입력, 확인
            # score_cal(1,score)  # 영어점수입력, 확인
            # # score_cal(2,score)  # 수학점수입력, 확인
            # --------- 위와 동일함(함수 입력했을 때)---------------------
            # while True:
            #     score[0]=input(f"{title[2]} 점수를 입력하세요.>> ")
            #     if score[0].isdigit():
            #         score[0]=int(score[0])         # 숫자변환
            #         if 0 <= score[0] <= 100:  # 0에서 100사이의 값인지 확인
            #             break
            #         else: print("점수는 0~100사이의 값을 입력하셔야 합니다.")
            #     else: print("숫자만 가능합니다.")
                
            # while True:
            #     score[1]=input(f"{title[3]} 점수를 입력하세요.>> ")
            #     if score[1].isdigit():
            #         score[1]=int(score[1])         # 숫자변환
            #         if 0 <= score[1] <= 100:  # 0에서 100사이의 값인지 확인
            #             break
            #         else: print("점수는 0~100사이의 값을 입력하셔야 합니다.")
            #     else: print("숫자만 가능합니다.")
            
            # while True:
            #     score[2]=input(f"{title[4]} 점수를 입력하세요.>> ")
            #     if score[2].isdigit():
            #         score[2]=int(score[2])
            #         if 0 <= score[2] <= 100:
            #             break
            #         else: print("점수는 0~100사이의 값을 입력하셔야 합니다.")
            #     else: print("숫자만 가능합니다.")