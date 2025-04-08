# 순서
# 1. sModule.py - class 2개
# 2. sMain.py
#  - sModule.py 사용해서 프로그램 구현
# 3. sFunc.py 함수를 옮겨봄.

from sModule import Student,Students
from sFunc import *




# 학생성적프로그램
while True:
    choice=tmenu_print()  # 상단메뉴부분    
    if choice == 1:  # 학생성적입력
        print("[ 학생성적입력 ]")
        name=input(f"{Student.count}번째 학생 이름을 입력하세요.>> ")
        score=[0]*3
        for i in range(len(score)):
            score[i]=int(input(f"{title[i+2]}점수를 입력하세요.>> "))
            
            