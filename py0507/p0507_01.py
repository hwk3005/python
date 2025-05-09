from stuFunc import *



while True:
    print("[ 학생성적프로그램 ]")
    print("-"*20)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적검색")
    print("4. 학생성적정렬")
    print("5. 학생성적 아이디,전화번호출력- member,stuscore조인")
    print("8. 등수처리")
    print("9. 등급처리")
    print("0. 프로그램종료")
    print("-"*20)
    choice = input("원하는 번호를 입력하세요.>> ")
    
    if choice == "1": # 학생성적입력
       stuInsert() ## 미구현
    elif choice == "2": # 학생성적출력
       stuAllSelect() 
    elif choice == "3":  # 학생성적검색
       stuSearch() 
    elif choice == "4":  # 학생성적정렬
       stuSort() 
    elif choice == "8":  # 등수처리
       rankUpdate() 
    elif choice == "9":  # 등급처리
       gradeUpdate()  
    else:
        break
    
print("프로그램을 종료합니다.")    
