# Q2. 구구단 출력하시오. 
# 2x1=2
# 9x1=9
i=0
for i in range(1,10):
    for j in range(2,10):
        print("{}x{}={}".format(j,i,i*j),end="\t")
    print()
    
# =>> 가로로 구구단 출력 ▼▼▼▼▼
# 2x1=2   3x1=3   4x1=4   5x1=5   6x1=6   7x1=7   8x1=8   9x1=9
# 2x2=4   3x2=6   4x2=8   5x2=10  6x2=12  7x2=14  8x2=16  9x2=18
# 2x3=6   3x3=9   4x3=12  5x3=15  6x3=18  7x3=21  8x3=24  9x3=27
# 2x4=8   3x4=12  4x4=16  5x4=20  6x4=24  7x4=28  8x4=32  9x4=36
# 2x5=10  3x5=15  4x5=20  5x5=25  6x5=30  7x5=35  8x5=40  9x5=45
# 2x6=12  3x6=18  4x6=24  5x6=30  6x6=36  7x6=42  8x6=48  9x6=54
# 2x7=14  3x7=21  4x7=28  5x7=35  6x7=42  7x7=49  8x7=56  9x7=63
# 2x8=16  3x8=24  4x8=32  5x8=40  6x8=48  7x8=56  8x8=64  9x8=72
# 2x9=18  3x9=27  4x9=36  5x9=45  6x9=54  7x9=63  8x9=72  9x9=81



# Q1. 은행가면 001 002 003...010 011 012...999
for i in range(0,1000):
    print("{:03d}".format(i))

import random

# a_list=random.sample(range(1,45+1),6)  ▼▼ 아래와 동일한 방법(파이썬만 가능)
ran_list=[]
i=0
while i<6:
    ran_input=random.randint(1,45)
    ran_input=int(input("{}번째 숫자를 입력하세요: ".format(i+1)))
    if ran_input not in ran_list:
        ran_list.append(ran_input)
        i+=1  # i=i+1
print(ran_list)