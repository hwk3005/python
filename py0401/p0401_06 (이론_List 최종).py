# 1. 리스트 삭제
a_list=[1,2,3,4,5,11,12,13]

del a_list[0]  # index번호를 가지고 삭제
a_list.pop()   # 마지막 데이터 삭제
a_list.pop(2)  # index번호 삭제
a_list.remove(2)  # 2라는 값을 삭제
a_list.remove(11)  # 데이터 11숫자 삭제
a_list.clear()  # 모두 삭제

print(a_list)
# -----------------
# 2. 리스트 추가
a_list.append(1)  # 리스트 마지막 추가
a_list.append(2)
a_list.insert(0,"홍길동")  # 원하는 위치에 데이터 추가
a_list.extend([10,11,12])  # 리스트 추가

print(a_list)
# -----------------
# 3. 리스트 수정
a_list[0]="유관순"

print(a_list)
# -----------------
# 4. 리스트 출력
for a in a_list:
    print(a)
# -----------------
# 5. 리스트에 여러데이터 묶음도 추가 가능 (리스트 안에 리스트 추가 가능)
a_list.append(['컴퓨터공학','소프트웨어공학','무역학과'])

# -----------------
# 6. 리스트 길이
print(len(a_list))

# -----------------
# 리스트 안에 해당 값의 개수 파악
s_list=[1,2,3,1,2,2,2,1,3,4,5,7,7,7,10,9,8]
print("{}:{}".format(1,s_list.count(1)))

# 위와 동일 ▼▼
num=0
for s in s_list:
    if s==1:
        num+=1
print("{}:{}".format(1,num))
# -----------------
# 리스트 정렬
s_list.sort()  # 순차/낮은순 정렬
print(s_list)
s_list.sort(reverse=True)  # 역순/높은순 정렬
# s_list.reverse()  # 역순/높은순 정렬
print(s_list)

