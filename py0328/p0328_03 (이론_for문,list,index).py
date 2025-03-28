# # 반복문을 사용해서 1~10까지 출력
# for i in range(1,11):
#     print(i)

# a=10
# if a>5 and a<9:  #True and False (둘다 참이면 True/하나라도 거짓이면 False)
#     print(a)
# if a>5 or a<9:  #True or False (하나라도 참이면 True)
#     print(a)

a_list=[1,2,3,4,5]
print(a_list[2])    # A. 3
# [:] 슬라이싱 (여러 개를 한꺼번에 출력)
print(a_list[1:4])  # [시작위치:끝나는위치]  ★★
print(a_list[:3])   # [:끝나는위치] (처음~끝나는위치까지 출력해라.)
print(a_list[2:])   # [시작위치:] (시작위치~끝까지 출력해라)
print(a_list[::2])  # [::끝나는위치] 2개씩 증가해서 출력
print(a_list[::-1]) # [::-1] 역순으로 출력  ★★
print(a_list[:-1])  # [:-1] 끝나는위치에서 -1  ★★

# ex. 
a="안녕하세요."
print(a[2])  # A. 하
print(a[1:4])
print(a[:3])
print(a[2:])
print(a[::-1])
print(a[:-1])

print(a[:7])  # 슬라이싱: 없는 값 출력시 => 에러가 나지 않음.
# print(a[7])  # 인덱싱: 없는 것 출력시 => 에러 IndexError

print(len(a_list))
print(a_list[:len(a_list)-1])
print(len(a))  # 문자열 길이

# a_list[1:11:2]
for i in range(1,11,2):
    print(i,end=" ")  # end="" 줄바꿈 없이 출력, # A. 1,3,5,7,9


# Q1. 합계가 100이 넘는 위치의 숫자는 얼마일까요?
# 1+2+3+4+5+6+7..... 합계가 100넘는 위치가 어디인지 출력하시오. 그때 값도 출력하시오.
#break
sum=0
i=0
for i in range(1,100+1):
    sum = sum+i
    print("i:{}, sum: {}".format(i,sum))
    if sum>=100: break
# print("1~100까지 합계: {}".format(sum))
print("sum이 100넘었을때 i값(위치): ",i)
print("합계가 100넘었을때 sum값: ",sum)



