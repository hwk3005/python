# # Q1. 좌표맞추기 프로그램을 구현하시오.

# 1차원 리스트 생성 후 랜덤 섞기


# 2차원 리스트 생성 후 1차원 리스트 값 넣기

# 2차원 출력

# 입력부분

# 좌표X로 값변경
















# ______________________________________

# # Q1. 좌표맞추기 프로그램을 구현하시오.
# import random
# # 1차 리스트 생성 후 랜덤 섞기
# first_list=[i+1 for i in range(25)]
# random.shuffle(first_list)

# # 2차 리스트 생성 후 1차 리스트 값 넣기
# second_list=[[0]*5 for i in range(5)]
# for i in range(5):
#     for j in range(5):
#         second_list[i][j]=first_list[5*i+j]

# # 2차원 형태 출력
# while True:
#     print("[ 좌표 맞추기 프로그램 ]")
#     print("-"*45)
#     print("*  |",end="\t")
#     for i in range(5):
#         print(i,end="\t")
#     print()
#     print("-"*45)
#     for i in range(5):
#         print(f"{i}  |",end="\t")
#         for j in range(5):
#             print(second_list[i][j],end="\t")
#         print()
        
#     # 입력값 받기
#     print("-"*45)
#     num=int(input("1~25번 숫자를 입력하시오: "))
    
#     # 좌표에 X값 표시
#     for i in range(5):
#         for j in range(5):
#             if second_list[i][j]==num:
#                 second_list[i][j]="X"
#     print()

# ______________________________________

# # Q1. 좌표맞추기 프로그램을 구현하시오.

# import random
# # 1차원 리스트 생성 후 랜덤 섞기
# first_list=[i+1 for i in range(25)]
# random.shuffle(first_list)

# # 2차원 리스트 생성 후 1차원 리스트 값 넣기
# second_list=[[0]*5 for i in range(5)]
# for i in range(5):
#     for j in range(5):
#         second_list[i][j]=first_list[5*i+j]

# # 2차원 형태로 출력
# while True:
#     print("     [ 좌표 맞추기 프로그램 ]")
#     print("-"*45)
    
#     print("* |",end="\t")
#     for i in range(5):
#         print(i,end="\t")
#     print()
#     print("-"*45)
    
#     for i in range(5):
#         print(f"{i}  |",end="\t")
#         for j in range(5):
#             print(second_list[i][j],end="\t")
#         print()

#     # 입력부분
#     print("-"*45)
#     num=int(input("1~25번 숫자를 입력하세요: "))
    
#     # 좌표에 X값 넣기
#     for i in range(5):
#         for j in range(5):
#             if second_list[i][j]==num:
#                 second_list[i][j]="X"
#     print()