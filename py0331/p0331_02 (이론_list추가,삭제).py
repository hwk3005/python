# 리스트 삭제: del, pop, remove, clear
a_list=[1,2,3,4,5]
del a_list[2]  # del 위치값 삭제
print(a_list)
a_list.pop()  # pop 맨 뒤 삭제, 특정위치 삭제
print(a_list)
a_list.remove(1)  # remove데이터값으로 삭제
print(a_list)
a_list.clear()  # clear 전체 삭제
print(a_list)
# ____________________________________________
## 리스트 추가 ★
# 리스트 추가: append,insert,extend
a_list=[1,2,3]
a_list.append(4)  # append 마지막에 추가
print(a_list)
a_list.insert(1,100) 
print(a_list)  # insert 특정위치에 값을 추가 (잘 안 씀_시간 오래걸림)
a_list.extend([100,200,300])  # extend 다른 리스트를 추가
print(a_list)

# 리스트 내포
a_list=[i for i in range(1,11)]
print(a_list)       # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 리스트 추가: append (명령어 추가하는 방법)
a_list=[]
for i in range(1,11):
    a_list.append(i)
print(a_list)       # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ____________________________________________

# < enumerate > index번호를 넣으려면 enumerate를 사용
a_list=[273,10,5,9,100,1000,50]
for idx,value in enumerate(a_list):
    print(f"{idx+1}: {value}")


