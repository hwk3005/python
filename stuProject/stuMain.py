from stuModule import Student,Students
from stuFunc import *  #함수,변수 모두다 가져옴

  
# 학생성적프로그램    
while True:
    choice = tmenu_print() # 상단메뉴부분
    if choice == 1:
        stu_input()     # 학생성적입력 함수
    elif choice == 2:
        stu_output()    # 학생성적출력 함수
    elif choice == 3:  
        stu_modify()    # 학생성적수정 함수
        




