a="홍길동님! 안녕하세요. 반갑습니다. 안녕 반가워.안녕안녕"
# a.find() # for,while문을 사용해서 안녕이 몇 번 나오는지 개수를 출력하시오.

i=0
count=0
while True:
    num=a[i:].find("안녕")
    if num != -1:   # 안녕이라는 글자가 있는 경우
        count += 1  # 개수 1증가
        i+=num+1
    else: break
print("개수: ",count)

# print(a[i:].find("안녕"))
# print(a[0+6+1:].find("안녕"))




# num=a.count("안녕")  # count함수 (파이썬에만 있음)
# print(num)

# 글자가 있는지 확인
# if "안녕" in a:
#     print("안녕이라는 글자가 있습니다.")

# 글자가 있으면 위치 알려줌.
# print(a.find("안녕"))
