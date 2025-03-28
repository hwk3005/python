# num=7
# if 10>=num>=0:      #파이썬만 가능.
#     print("10에 해당되는 숫자입니다.")


# if 10>=num and num>=0:      #다른 프로그램은 이렇게 가능.
#     print("10에 해당되는 숫자입니다.")


# Q1. 숫자를 입력받아 봄,여름,가을,겨울을 출력하시오.
# 3,4,5 → 봄의 계절입니다.
# 6,7,8 → 여름의 계절입니다.
# 9,10,11 → 가을의 계절입니다.
# 12,1,2 → 겨울의 계절입니다.
season=int(input("월(月)을 숫자로 입력하시오: "))
if season>=3 and season<=5:
    print("봄의 계절입니다.")
elif season>=6 and season<=8:
    print("여름의 계절입니다.")
elif season>=9 and season<=11:
    print("가을의 계절입니다.")
elif season==12 or season<=2:
    print("겨울의 계절입니다.")
else:
    print("존재하지 않는 월(月)입니다.")





    





