# Q3. 구구단 출력
# Q3-1. 기본
for i in range(2,9+1):
    print("[ {} 단 ]".format(i))
    for j in range(1,9+1):
        print("{}x{}={}".format(i,j,i*j),end=" ")
    print()
# Q3-2. 3,5,7,9단 홀수단만 출력하시오.
for i in range(2,9+1):
    if i%2==1:
        print("[ {} 단 ]".format(i))
        for j in range(1,9+1):
            print("{}x{}={}".format(i,j,i*j),end=" ")
        print()


# Q3-3. 시작단과 끝나는 단을 입력받아, 출력하시오.
#   ex. 2, 6 → 2~6단까지 출력
num1=int(input("시작단을 입력하세요: "))
num2=int(input("끝나는 단을 입력하세요: "))

if num1>num2:
    num1,num2=num2,num1  # 파이썬만 가능

for i in range(num1,num2+1):
    print("[ {} 단 ]".format(i))
    for j in range(1,9+1):
        print("{}x{}={}".format(i,j,i*j))
    print()


# Q1. 두 수를 입력받아, 두수 사이의 합계를 구하시오.
#   ex. 1,7 → 1,2,3,4,5,6,7까지 합을 출력하면 됨.
num1=int(input("숫자를 입력하세요: "))
num2=int(input("숫자를 입력하세요: "))
print(num1,num2)

# if문 비교 (num1,num2) num2가 더 큰지 확인
if num1>num2:
    t=num1              # (모든 프로그램 가능)
    num1=num2
    num2=t
    # num1,num2=num2,num1 (파이썬만 가능)
sum=0
for i in range(num1,num2+1):
        sum=sum+i
        print("i: {}, sum: {}".format(i,sum))
print("{}에서 {}까지의 합계: {}".format(num1,num2,sum))






