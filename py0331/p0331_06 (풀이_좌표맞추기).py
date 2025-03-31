
# x좌표: 1
# y좌표: 3
# 1,3 → 문자 인식

# num1=int(input("X좌표: "))
# num2=int(input("Y좌표: "))
# print(f"[X,Y좌표: {num1},{num2}]")

num=input("X,Y좌표 (0,0): ")  # 1,3,5,7
n_list=num.split(",")  # split (쉼표나 띄어쓰기 등 기호로 구분해서 분리함 )
print(f"[X,Y좌표: {n_list}]")  # ['1', '3', '5', '7']

