# choice 3 학생성적수정 부분 설명


#        0      1     2      3      4
title=["번호","이름","국어","영어","수학","합계","평균","등수"]

while True:
    print("1. 국어입력")
    print("2. 영어입력")
    print("3. 수학입력")
    choice=int(input("원하는 번호를 입력하세요.>> "))
    
    if choice==1:
        print(f"[ {title[choice+1]}성적 입력 ]")  # {title[2]} == choice1+1 = 2
    elif choice==2:
        print(f"[ {title[choice+1]}성적 입력 ]")  # {title[3]}
    elif choice==3:
        print(f"[ {title[choice+1]}성적 입력 ]")
        
        