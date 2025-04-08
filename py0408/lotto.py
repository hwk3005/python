# lotto 프로그램
import random









# # ------------------------------------------------------------------
# # p0328_08.py 참고

# ran_list=random.sample(range(1,45+1),6)  # 랜덤번호 6개 리스트
# my_list=[]     # 입력번호 저장 리스트
# lotto_count=0  # 당첨개수
# lotto_list=[]  # 당첨번호

# i=0
# while i<6:
#     print(f"랜덤번호: {ran_list}")                          # 랜덤번호
#     my_input=int(input(f"{i+1}번째 숫자를 입력하세요.>> "))  # 입력번호
#     if my_input not in my_list:
#         my_list.append(my_input)  # 입력번호 추가
#         i+=1

# for j in range(6):
#     if ran_list[j] in my_list:
#         lotto_count+=1
#         lotto_list.append(ran_list[j])

# print()
# print(f"랜덤번호: {ran_list}")
# print(f"입력번호: {my_list}")
# print(f"당첨개수: {lotto_count}")
# print(f"당첨번호: {lotto_list}")
