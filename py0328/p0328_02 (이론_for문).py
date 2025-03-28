print("안녕하세요.")
print("안녕하세요.")
print("안녕하세요.")

# for문 (반복문)

# range(3) → 0,1,2 (0부터 시작해서 3번 돌음)
for i in range(3):
    print("안녕하세요.",i)
    
# range(1,4) → 1,2,3 (1부터 4앞에까지 출력)
for i in range(1,4):
    print("안녕하세요.",i)
    
# range(1,3+1) → 1,2,3
for i in range(1,3+1):
    print("안녕하세요.",i)
    
# range(1,11,2) → (시작번호, 마지막번호 앞까지, 간격) ★★★
for i in range(1,11,2):
    print("안녕",i)
    
# range() 자리에 list타입도 가능
a_list=[1,2,3,4,5]
for i in a_list:
    print("안녕",i)


