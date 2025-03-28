# Q1. 1,3,5,7,9......99  1-100사이의 홀수만 숫자를 더해서 합계를 구하시오.
sum=0
for i in range(1,100+1,2):
    sum=sum+i
print("합계: ",sum)


# Q2. 1-100까지의 숫자 중, 3의 배수만 더해서 sum을 구하시오. 
# if i%3 == 0

# Q2-1. 1-100까지의 숫자의 합을 구하시오.
# Q2-2. 3의 배수 조건 추가
sum=0
for i in range(1,100+1):
    if i%3==0 and i%5==0:      # 3의 배수이면서, 5의 배수인 것.
        sum=sum+i
        print("i:{}, sum:{}".format(i,sum))
print("합계: ",sum)

# Q2-3. 3 또는 7의 배수의 합
sum=0
for i in range(1,100+1):
    if i%3==0 or i%7==0:
        sum=sum+i
        print("i: {}, sum: {}".format(i,sum))
print("합계: ", sum)


