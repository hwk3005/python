# ---------------------------------
# Chapter 02 자료형 (print, input, 변수, 자료형, 연산자, format,f문자열 등)


# print("안녕")

# p70 -- 키워드 출력 (변수로 사용 불가능) --
# import keyword
# print(keyword.kwlist)
# p71 -- 식별자 identifier : 프로그래밍 언어에서 이름을 붙일 때 사용하는 단어
# 키워드 사용x, 특수문자 _만 허용, 숫자로 시작x, 공백 포함x
# 식별자 - 캐멀케이스(대문자로시작) - 클래스
#       - 스네이크케이스(소문자로시작) - 함수(뒤에 괄호o)/변수(뒤에 괄호x)

# p76 -- print --
# 여러 개 출력
# print(52,273,"Hello")
# 줄바꿈
# print()

# p84 -- 자료형: 자료의 형식(data type) / 자료(프로그램이 처리할 수 있는 모든 것)
# print(type("안녕하세요."))  # string 문자열
# print(type(273))          # integer 정수
# print(type(52.345))         # float 실수형
# print('"안녕하세요"라고 말했습니다.')
# print("\"안녕\"이라고 말했습니다.")
# print("안녕하세요\n안녕하세요\t안녕")
# print("""1. 동해물과 백두산이 마르고 닳도록
# 하느님이 보우하사 우리나라 만세
# 무궁화 삼천리 화려 강산
# 대한 사람 대한으로 길이 보전하세""")
# print("안녕"+"하세요")
# print("안녕하세요"*3)

# p95 -- 인덱싱(문자선택연산자): []
# print("안녕하세요"[0])
# print("프린트"[1])
# print("프린트"[-1])
# p96 -- 슬라이싱(문자열범위선택연산자): [:]
# print("안녕하세요"[1:4])    # 녕하세
# print(len("안녕하세요"))

# 숫자연산자: 사칙 +-*/, 몫//, 나머지%, 제곱**
# print("5+7=",5+7)
# print("3//2=",3//2)
# print("4%2=",4%2)
# print("2**3=",2**3)
# 서로 다른 자료 연산 시 TypeError 발생

# p112 -- 변수: 값을 저장할 때 사용하는 식별자
# pi = 3.1415
# print(pi)

# p116 -- 복합대입연산자 += -= *= /= %= **=
# string="안녕하세요"
# string += "!"
# string += "!"
# print("string:",string)

# p118 -- input 사용자입력
# string = input("인사말을 입력하세요>> ")
# print(string)
# print(type(string))

# p121 -- cast/casting 형변환, type변경
# 문자열 -> 숫자로 캐스팅
# string_a = input("입력A> ")
# int_a = int(string_a)
# string_b = input("입력B> ")
# int_b = int(string_b)
# print("문자열자료:",string_a + string_b)
# print("숫자자료:",int_a + int_b)
# 숫자 -> 문자열 캐스팅
# output_a = str(52)
# output_b = str(52.273)
# print(type(output_a),output_a)
# print(type(output_b),output_b)
# inch -> cm 단위로 변경
# raw_input = input("inch 단위의 숫자를 입력해주세요: ")
# inch = int(raw_input)
# cm = inch * 2.54
# print(inch,"inch ->",cm,"cm")

# p135 -- 문자열의 format() 함수
# format() 함수로 숫자->문자열 변환하기
# string_a = "{}".format(10)
# print(type(string_a),string_a)
# 예제1
# format_a = "{}만원".format(5000)
# format_b = "파이썬 열공하여 첫 연봉 {}만원 만들기".format(5000)
# format_c = "{} {} {}".format(3000,4000,5000)
# format_d = "{} {} {}".format(1,"문자열",True)
# print(format_a)
# print(format_b)
# print(format_c)
# print(format_d, type(format_d))
# 예제2
# output_a = "{:d}".format(52)
# output_b = "{:5d}".format(52)
# output_c = "{:05d}".format(52)
# print("기본>>",output_a)
# print("특정칸에 출력>>",output_b)
# print("빈칸 0으로 채우기>>",output_c)
# 예제3
# output_f = "{:+d}".format(52)
# output_g = "{:+d}".format(-52)
# print(output_f)
# print(output_g)
# p139 -- 예제4
# output_h = "{:+5d}".format(52)
# output_j = "{:=+5d}".format(52)
# print(output_h)
# print(output_j)
# p140 -- 예제5,6_부동소수점출력
# output_a = "{:f}".format(52.273)
# output_b = "{:15.3f} {:+15.2f}   {:+015.1f}".format(52.273,52.273,52.273)
# print(output_a)
# print(output_b)
#p141 -- 예제7_의미없는 소수점제거  {:g}
# output_a = 52.00
# output_b = "{:g}".format(output_a)
# print(output_a)
# print(output_b)

# p141 -- 대소문자 바꾸기: upper(), lower()
# a = "Hello Python"
# print(a.upper())
# print(a.lower())

# p142 -- 문자열 양옆 공백제거: strip()
# input_a = """
#     안녕하세요.
# 문자열 함수    
# """
# print(input_a.strip())

# p143 -- 문자열 구성 파악: is00() : isalnum(), isalpha(), isdigit(), isidentifier(), isdecimal()
# print("TrainA10".isalpha())
# print("10".isdigit())

# p144 -- 문자열 찾기: find() 왼쪽부터 찾아서 처음 등장하는 위치 찾음, rfind() 오른쪽부터 , 01234..
# output_a = "안녕안녕하세요".find("안녕")
# output_b = "안녕안녕하세요".rfind("안녕")
# print("{}\t{}".format(output_a,output_b))

# p145 -- in연산자: 문자열내부에 어떤 문자열이 있는지 확인할 때
# print("잘자" in "안녕하세요")

# p145 -- 문자열 자르기: split()  => 실행결과로 list 나옴
# a = "10 20 30 40 50".split(" ")
# b = "10,20,30,40,50".split(",")
# print(a)
# print(b)

# p146 -- f 문자열
# 예제1
# a = 10.39459
# print("{:.2f}".format(a))
# print(f"{a:.2f}")
# 예제2
# print(f"3+4={3+4}")
# print(f"""
#       1+2={1+2}
#       2+3={2+3}
#       3+4={3+4}""")
# 예제3
# 1) format
# data = ["별",2,"M","서울특별시 강서구","Y"]
# print("""
#       이름: {}
#       나이: {}
#       성별: {}
#       지역: {}
#       중성화여부: {}""".format(*data))  # 전개연산자 : *
# 2) f 문자열
# print(f"""
#       이름: {data[0]}
#       나이: {data[1]}
#       성별: {data[2]}
#       지역: {data[3]}
#       중성화여부: {data[4]}""")

