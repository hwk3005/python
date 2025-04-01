# 1차원 리스트
import random
s_list=[i for i in range(1,26)]  # 1차원 리스트 생성
# s_list=[i+1 for i in range(25)]  # 위와 동일한 답 출력됨
random.shuffle(s_list)
# random.random(), random.randint(), random.sample(), random.shuffle()

# 2차원 리스트
my_list=[[0]*5 for _ in range(5)]  # 2차원 리스트 생성
# my_list[0][1]=1  # 값 변경

# 1차원 리스트 값 → 2차원 리스트 입력
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
    
    # 번호입력 X표시
    num=int(input("1~25번 숫자를 입력하세요: "))    
    # 25개 모두 비교
    stop=0
    for i in range(5):
        for j in range(5):
            if my_list[i][j]==num:
                my_list[i][j]="X"
                stop=1
                break
        if stop==1:break
    print()

    # 좌표입력
    # x=int(input("X좌표를 입력하세요: "))
    # y=int(input("Y좌표를 입력하세요: "))
    # my_list[y][x]="X"