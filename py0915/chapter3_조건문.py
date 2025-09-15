# ---------------------------------
# Chapter 03 조건문


# p157 -- 불 자료형 Boolean 불린: 값 True, False만 가짐
# 1) 비교연산자 활용
# 예제1
# print(10 == 100)
# print(10 != 100)
# print(10 > 100)
# 예제2
# print("가방"=="가방")
# print("가방"!="하마")
# print("가방">"하마")  # 가나다순(뒤로갈수록 큼)
# 예제3
# x = 25
# print(10 < x < 30)
# print(40 < x < 60)
# 2) 논리연산자 활용
# 예제4 -- not
# print(not True)
# print(not False)
# 예제5 -- not
# x = 10
# under_20 = x < 20   # True
# print("under_20: ",under_20)
# print("not under_20: ",not under_20)
# 예제6 -- and, or
# print(True and True)
# print(True and False)
# print(True or False)
# print(False or True)


# p164 -- if조건문

# 예제1 -- 기본
# number = int(input("정수 입력>> "))
# if number > 0 :
#     print("양수입니다.")
# if number < 0 :
#     print("음수입니다.")
# if number == 0 :
#     print("0입니다.")

# 예제2 -- 날짜/시간 한 줄로 출력
# import datetime
# now = datetime.datetime.now()
# print("{}년 {}월 {}일 {}시 {}분 {}초".format(
#     now.year, now.month, now.day, now.hour, now.minute, now.second ))

# 예제3 -- 오전/오후 구분
# import datetime
# now = datetime.datetime.now()
# if now.hour < 12: print("현재 시각은 {}시로 오전입니다.".format(now.hour))
# if now.hour >=12: print(f"현재 시각은 {now.hour}시로 오후입니다.")

# 예제4 -- 계절 구분
# import datetime
# now = datetime.datetime.now()
# if 3 <= now.month <= 5: print(f"이번 달은 {now.month}월로 봄입니다.")
# if 6 <= now.month <= 8: print(f"이번 달은 {now.month}월로 여름입니다.")
# if 9 <= now.month <= 11: print("이번 달은 {}월로 가을입니다.".format(now.month))
# if now.month == 12 or 1 <= now.month <= 2: print("이번 달은 {}월로 겨울입니다.".format(now.month))

# p170 -- 예제5 -- 끝자리로 짝수, 홀수 구분
# number = input("정수 입력>> ")
# last_number = int(number[-1])
# if last_number == 0 \
#     or last_number == 2 \
#     or last_number == 4 \
#     or last_number == 6 \
#     or last_number == 8:
#     print("짝수입니다.")
# else:
#     print("홀수입니다.")
### if last_number == 0 or 2 or 4 or 6 or 8     # 사용할 수 없는 코드

# 예제6 -- in 문자열 연산자 활용해서 짝수, 홀수 구분
# number = input("정수 입력>> ")
# last_number = number[-1]
# if last_number in "02468": print("짝수입니다.")
# if last_number in "13579": print("홀수입니다.")

# p171 -- 예제7 -- 나머지 연산자 활용해서 짝수, 홀수 구분
# number = int(input("정수 입력>> "))
# if number % 2 == 0: print("짝수입니다.")
# if number % 2 == 1: print("홀수입니다.")

# p177 -- 예제8 -- else
# number = int(input("정수 입력>> "))
# if number%2 == 0: print("짝수입니다.")
# else: print("홀수입니다.")

# p178 -- 예제9 -- elif
# import datetime
# now = datetime.datetime.now()
# month = now.month
# if 3 <= month <= 5: print("현재는 봄")
# elif 6 <= month <= 8: print("현재 여름")
# elif 9 <= month <= 11: print("현재 가을")
# else: print("현재 겨울")

# p181 -- 예제10 -- elif
# score = float(input("학점 입력>> "))
# if score == 4.5: print("신")
# elif 4.2 <= score: print("교수님의 사랑")
# elif 3.5 <= score: print("현 체제의 수호자")

# p182 -- 예제11 -- False로 변환되는 값
# # 1) if 조건문에 0 넣기
# if 0: print("0은 True로 변환됨")
# else: print("0은 False로 변환됨")
# # 2) if 조건문에 빈 문자열 넣기
# if "": print("빈 문자열은 True로 변환됨")
# else: print("빈 문자열은 False로 변환됨")

# p184 -- 예제12 -- pass키워드_미구현부분 건너뛰기
# number = int(input("정수 입력>> "))
# if number > 0: pass
# else: pass

# p185 -- raise NotImplementedError : 임의로 에러처리(추후 확인용)
# number = int(input("정수 입력>> "))
# if number > 0: raise NotImplementedError
# else: raise NotImplementedError


