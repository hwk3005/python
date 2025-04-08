# p0401_01.py 참고

# (좌표)숫자맞추기 프로그램
import random
s_list=[i for i in range(1,26)]  # 1차원 리스트 생성 (1~25 숫자)
random.shuffle(s_list)  # 랜덤으로 섞기

# 2차원 리스트에 1차원리스트 값을 넣기
my_list=[[0]*5 for _ in range(5)]
for i in range(5):
    for j in range(5):
        my_list[i][j]=s_list[5*i+j]

# 화면 출력
while True:
    print(" "*10,end="")
    print("[ 좌표 맞추기 프로그램 ]")
    print("-"*45)
    print("*  |",end="\t")
    for i in range(5):
        print(i,end="\t")
    print()
    print("-"*45)
    for i in range(5):
        print(f"{i}  |",end="\t")
        for j in range(5):
            print(my_list[i][j],end="\t")
        print()
    print("-"*45)
    
    # 번호 입력
    num=int(input("1~25번 숫자를 입력하세요.>> "))
    # 입력된 번호에 맞는 위치 X표시
    stop=0
    for i in range(5):
        for j in range(5):
            if my_list[i][j]==num:
                my_list[i][j]="X"
                stop=1
                break
        if stop==1:break
    print()
