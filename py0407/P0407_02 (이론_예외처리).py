# 예외처리
# 프로그램을 하다보면, 에러

# 1. 구문에러
# 2. 런타임 에러

print("데이터 출력")
# print("데이터 출력")  # 구문에러 - 오타

a_list = [1,2,3,4,5]
for a in a_list:
    print(a)

# # 런타임 에러
# for i in range(6):
#     print(a_list[i]) # 구문에 에러는 없지만 실행시 에러 - 런타임에러  

#- 프로그램이 종료     

# 에러를 처리하는 방법 - 1. if조건문을 사용해서 처리, 2.예외처리 사용
# 1. if조건문
print("1. 학생성적출력")
choice = input("원하는 번호를 입력하세요.>> ")
# 숫자로 변환 가능한지 확인
if choice.isdigit():
    choice = int(choice)
else:
    print("숫자만 입력이 가능합니다.")
print("입력한 번호 : ",choice) 

# 2. 예외처리 - try
print("1. 학생성적출력")
choice = input("원하는 번호를 입력하세요.>> ")
# 숫자로 변환 가능한지 확인
# 예외처리 - 강제로 프로그램이 종료되는 문제를 해결, 에러에 대한 문제점 확인
try: 
    choice = int(choice)
except Exception as e:
    print("숫자만 입력이 가능합니다.")
    print(e) # 에러의 구문 출력가능
print("입력한 번호 : ",choice)    