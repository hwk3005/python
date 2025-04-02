# API, CSV, Json, XML, html
# CSV: 쉼표(,)로 구분된 값(Comma-Separated Values)을 저장한 텍스트 파일 형식
# ___________________________________________________________________________
# 문자열
# isdigit / isalpha / isalnum / islower / isupper 
# map / join / split/ replace / strip / count / find/ endswith /
# upper / lower / swapcase / title / len
# center(중앙정렬) / ljust(좌측정렬) / rjust(우측정렬) / zfill(채우기)



# _________________________
# print('1234'.isdigit())    # 정수인지 확인
# print('abc'.isalpha())     # 알파벳인지 확인 - 한글 불가능
# print('abc123'.isalnum())  # 모두 숫자인지 확인 - abc,a1,123 모두 가능
# print('abc'.islower())     # 모두 소문자인지 확인
# print('ABC'.isupper())     # 모두 대문자인지 확인
# _________________________
# a="1234"
# if a.isdigit():  # 숫자로 변환가능 
#     print("숫자로 가능합니다.")  
# my=int(input("숫자를 입력하세요.>> "))
# while True:  
#     my_input=input("숫자를 입력하세요.>> ")
#     if my_input.isdigit():
#         my_input=int(my_input)
#     else:
#         print("숫자가 아닙니다. 숫자를 입력하세요.")
# _________________________
# score=['100','99','90']
# # 함수
# def cal(x):
#    return int(x)*100

# # map 한꺼번에 다 형변환 가능=> map(함수,데이터값)
# s_list=list(map(cal,score))
# print(s_list)

# sum=0
# for s in score:
#     sum+=int(s)  # 형변환 str → int
# print("합계: ",sum)
# _________________________
# txt=","
# txt2=txt.join("안녕하세요")  # join()글자 사이에 txt넣음
# print(txt2)
# _________________________
# 데이터베이스(DB)는 리스트를 저장할 수 없음. => 문자열로 저장함.

# txt="1,홍길동,100,100,100,300,100.0,1"
# print(txt)               # 1,홍길동,100,100,100,300,100.0,1
# txt_list=txt.split(",")  # ['1', '홍길동', '100', '100', '100', '300', '100.0', '1']
# print(txt_list)
# txt_list[1]='유관순'      # ['1', '유관순', '100', '100', '100', '300', '100.0', '1']
# print(txt_list)

# txt="a,b,c,d,안녕,반가워"
# txt_list=txt.split(",")
# print(txt_list)
# _________________________
# txt="  안녕하 세요  "
# print(txt.replace(" ",""))  # 문자를 다른 문자로 취환 => txt.replace(바꿀문자,취환할문자)
# txt2="파이썬 공부가 쉬워요~ 너무 쉬워요. 파이썬은 재미있어요"
# print(txt2.replace("파이썬","자바"))
# txt3="----파이썬----"
# print(txt3.strip("-"))  # 특정글자 제거
# print(txt3.replace("-","")) 

# print(txt)
# print(txt.strip())  # 공백제거 - 앞뒤:strip(), 오른쪽: rstrip(), 왼쪽: lstrip()
# _________________________
# txt="파이썬 공부가 쉬워요~ 너무 쉬워요. 파이썬은 재미있어요"
# print(txt.count("파이썬"))  # 문자열의 검색하려고 하는 글자 개수
# print(txt.count("요"))
# print(txt.find("공부"))  # 찾아서 있을 때: index번호 (글자 위치 알려줌.)
# print(txt.find("자바"))  # 찾아서 없을 때: -1
# t="aaa.py"
# print(t.endswith("py"))  # (파일명 맨끝글자가 일치하면) 있으면 True, 없으면 False
# _________________________
# txt="abBBcDd"         # 대소문자
# print(txt.upper())    # 대문자 출력
# print(txt.lower())    # 소문자 출력
# print(txt.swapcase()) # 대문자→소문자, 소문자→대문자
# print(txt.title())    # 단어 첫글자 다 대문자 변경해줌
# _________________________
# txt="안녕하세요"
# a_list=[1,2,3,4,5]

# print(a_list[1:3])  # 2,3
# print(txt[1:3])     # 녕하
# print(txt[2:])      # 하세요 (2부터 끝까지)
# print(txt*3)
# print("-"*50)
# print(len(txt))     # 글자길이 출력함
# print(txt[::-1])    # 글자역순 출력함

# # 문자열 index번호 가짐.
# print(txt[1])
# print(a_list[1])