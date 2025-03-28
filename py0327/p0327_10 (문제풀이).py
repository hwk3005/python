# Q1. 1~100까지 랜덤숫자를 생성해서 정답을 맞추는 프로그램을 구현하시오.
# 도전 횟수: 5
# 도전 번호: [1,2,3,4,5]
# 랜덤 번호: 5

# << 작업 순서 >>
#  1) 랜덤숫자 생성
#  2) num list 생성
#  3) n 변수 생성
#  4) 10번 for문 생성
#  5) num list에 저장
#  6) 정답비교
#  7) 데이터 출력

import random
num=[]
ran_num=random.randint(1,100)
n=0
for n in range(1,11):
    in_num=int(input("숫자를 입력하세요: "))
    num.append(in_num)
    if ran_num == in_num:
        print("정답입니다. 랜덤숫자: {}".format(ran_num))
        break
    elif ran_num>in_num:
        print("더 큰 수를 입력하세요. 입력숫자: {}".format(in_num))
    else:
        print("더 작은 수를 입력하세요. 입력숫자: {}".format(in_num))

print("도전 횟수: {}".format(n))
print("도전 번호: {}".format(num))
print("랜덤 번호: {}".format(ran_num))

