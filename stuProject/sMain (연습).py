# 순서
# 1. sModule.py - class 2개
# 2. sMain.py
#  - sModule.py 사용해서 프로그램 구현
# 3. sFunc.py 함수를 옮겨봄.

from sModule import Student,Students
from sFunc import *


# 학생성적프로그램
while True:
    def tmenu_print(): # 상단메뉴부분
        print(" "*20)
        print("[ 학생성적처리 프로그램 ]")
        print("-"*50)
        print("1. 학생성적입력")
        print("2. 학생성적출력")
        print("0. 프로그램 종료")
        choice=0
        try:
            choice=int(input("원하는 번호를 입력하세요.>> "))
        except Exception as e: print(e)
        return choice
    
    # 학생성적입력 함수선언