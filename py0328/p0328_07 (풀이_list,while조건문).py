# Q3. 입력한 숫자를 5번 반복해서 리스트에 추가하는 프로그램 구현

num_list=[]

# for반복문 사용
for i in range(10):
    num=int(input("숫자를 입력하세요: "))
    # num가 num_list에 여부 확인비교 (부(不)-입력, 여-제외)
    if num not in num_list:
        num_list.append(num)

# while반복문 사용
i=0
while i<10:
    num=int(input("{}번쨰 숫자를 입력하세요: ".format(i+1)))
    if num not in num_list:
        num_list.append(num)
        i+=1  # i=i+1    
print(num_list)

# if num in num_list:  
#         pass         == if num not in num_list:
#     else:
#         num_list.append(num)


# Q2.
input_list=[1,5,10,9,8,20]

a=5
if a in input_list:  # input_list안에 a가 있는지 확인
    print("{}가 존재합니다.".format(a))
else:
    print("{}가 존재하지 않습니다.".format(a))


# Q1.
i=0
# 반복문 while (조건식이 맞으면 (무한)반복)
while i<10:
    print(i)
    i += 1  # 1씩 증가

# 반복문 for (횟수만큼 반복)
for j in range(10):
    print(j)
 
