# ---------------------------------
# Chapter 06 예외처리


# ======================================
# ----- 06-1 구문 오류와 예외 -----
# ======================================
# 프로그램 작성할 때 항상 예외적인 상황까지 모두 생각하는 습관 기르기

# 프로그래밍 언어의 오류error 종류
#  - 구문 오류 syntax error : 프로그램 실행 전에 발생하는 오류
#  - 예외 exception / 런타임 오류 runtime error : 프로그램 실행 중에 발생하는 오류

# 1) 구문 오류 - 괄호의 개수, 들여쓰기 문제 등으로 실행 전에 발생 => 코드 수정해서 해결해야 프로그램 실행됨
# print("프로그램이 시작되었습니다.")
# print("# 예외를 강제로 발생시켜 보기! )  # SyntaxError: unterminated string literal (detected at line 13)

# 2) 예외 or 런타임오류
# print("# 프로그램이 시작되었습니다.")
# # list_a = [1,2,3,4,5]    # 예외 발생 코드 해결
# list_a[1]  # NameError: name 'list_a' is not defined. Did you mean: 'list'?

# 기본 예외 처리 : 예외를 해결하는 것 exception handling
#  ㄴ 방법: 조건문 / try구문 사용

# 예외 예시 코드
# number_input_a = int(input("정수 입력> "))    # ValueError: invalid literal for int() with base 10: '7센티미터'
# print("원의 반지름:", number_input_a)
# print("원의 둘레:", 2 * 3.14 * number_input_a)
# print("원의 넓이:", 3.14 * number_input_a * number_input_a)

# ======================================
# p365 ----- 기본 예외 처리 - 조건문 사용 -----
# ======================================
# 예제1 -- 조건문으로 예외 처리하기 - isdigit() 문자열 함수 사용
# user_input_a = input("정수 입력> ")
# if user_input_a.isdigit():
#     number_input_a = int(user_input_a)
#     print("원의 반지름:", number_input_a)
#     print("원의 둘레:", 2 * 3.14 * number_input_a)
#     print("원의 넓이:", 3.14 * number_input_a * number_input_a)
# else:
#     print("정수를 입력하지 않았습니다.")

# ======================================
# p366 ----- 기본 예외 처리 - try except (else) 구문 사용 -----
# ======================================
    # try: 예외가 발생할 가능성이 있는 코드
    # except: 예외가 발생했을 때 실행할 코드 or pass키워드
    # (else: 예외가 발생하지 않았을 때 실행할 코드) => 파이썬, 루비에만 있음 (자바, C언어 등에 없음)
    # (finally: 무조건 실행할 코드)
        # 조합 종류: try + except / try + except + else / try + except + finally / try + except + else + finally  / try + finally
        #  ㄴ 이 외의 조합 -> 구문 오류 발생함.

# 예제1 -- try except 구문
# try:
#     number_input_a = int(input("정수입력>> "))  # 예외 발생 가능성 있는 구문
#     print("원의 반지름:", number_input_a)
#     print("원의 둘레:", 2 * 3.14 * number_input_a)
#     print("원의 넓이:", 3.14 * number_input_a * number_input_a)
# except:
#     print("무언가 잘못되었습니다.")

# 예제2 -- try except + pass키워드 조합 : 숫자로 변환되는 것들만 리스트에 넣기
# list_input_a = ["52", "273", "32", "스파이", "103"]
# list_number = []  # 결과값 저장리스트
# for item in list_input_a:
#     try:
#         float(item)
#         list_number.append(item)
#     except:
#         pass
# print(f"{list_input_a} 내부에 있는 숫자는")
# print("{}입니다.".format(list_number))

# 예제3 -- try except else 구문
# try:
#     number_input_a = int(input("정수 입력>> "))
# except:
#     print("정수를 입력하지 않았습니다.")
# else:
#     print("원의 반지름:", number_input_a)
#     print("원의 둘레:", 2 * 3.14 * number_input_a)
#     print("원의 넓이:", 3.14 * number_input_a * number_input_a)

# ======================================
# p370 ----- finally 구문 ----- (거의 쓰지 x)
# ======================================
# 예제1 -- finally 구문
# try:
#     number_input_a = int(input("정수 입력>> "))
#     print("원의 반지름:", number_input_a)
#     print("원의 둘레:", 2 * 3.14 * number_input_a)
#     print("원의 넓이:", 3.14 * number_input_a * number_input_a)
# except:
#     print("정수를 입력하지 않았습니다.")
# else:
#     print("에외가 발생하지 않았습니다.")
# finally:
#     print("일단 프로그램이 어떻게든 끝났습니다.")

# ======================================
# p372 ----- finally에 대한 오해 -----
# ======================================
# 예제1 -- 파일이 제대로 닫혔는지 확인하기, 중간에 예외 발생
# try:
#     file = open("info.txt","w")
#     예외.발생해라()     # 파일 처리 중간에 예외 발생
#     file.close()
# except:
#     print("오류가 발생했습니다.")
# print("# 파일이 제대로 닫혔는지 확인하기")  # file.closed: False
# print("file.closed:", file.closed)

# 예제2 -- finally 구문 사용해 파일 닫기
# try:
#     file = open("info.txt","w")
#     예외.발생해라()
# except:
#     print("오류가 발생했습니다.")
# finally:
#     file.close()
# print("# 파일이 제대로 닫혔는지 확인하기")  # file.closed: True
# print("file.closed:", file.closed)

# 예제3 -- try except 구문 끝난 후 파일 닫기
# try:
#     file = open("info.txt","w")
#     예외.발생해라()
# except:
#     print("오류가 발생했습니다.")
# file.close()
# print("# 파일이 제대로 닫혔는지 확인하기")  # file.closed: True
# print("file.closed:", file.closed)

# ======================================
# p376 ----- finally 사용해서 깔끔한 코드 작성하는 경우 -----
# ======================================
# 예제1 -- try 구문 내부에서 return 키워드를 사용하는 경우
# def test():
#     print("test() 함수의 첫 줄입니다.")
#     try:
#         print("try 구문이 실행되었습니다.")
#         return
#         print("try 구문의 return 키워드 뒤입니다.")
#     except:
#         print("except 구문이 실행되었습니다.")
#     else:
#         print("else 구문이 실행되었습니다.")
#     finally:
#         print("finally 구문이 실행되었습니다.")
#     print("test() 함수의 마지막 줄입니다.")
# test()

# 예제2 -- finally 키워드 활용 - return 사용
# def write_text_file(filename, text):
#     try:
#         file = open(filename, "w")
#         file.write(text)
#         return
#     except:
#         print("오류가 발생했습니다.")
#     finally:
#         file.close()
# write_text_file("text.txt","안녕하세요.")

# 예제3 -- 반복문과 함께 사용하는 경우 - break 사용해서 try구문 빠져나가도 finally 실행됨
# print("프로그램이 시작되었습니다.")
# while True:
#     try:
#         print("try 구문이 실행되었습니다.")
#         break
#         print("try 구문의 break 키워드 뒤입니다.")
#     except:
#         print("except 구문이 실행되었습니다.")
#     finally:
#         print("finally 구문이 실행되었습니다.")
#     print("while 반복문의 마지막 줄입니다.")
# print("프로그램이 종료되었습니다.")

# ======================================
# p379 ----- 마무리 문제 -----
# ======================================
# 문제 1 -- 구문 오류와 예외의 차이를 설명하시오.
# 프로그램 실행전/후 발생 차이

# 문제 2 -- 예외처리 - 조건문, try except구문
# numbers = [52,273,32,103,90,10,275]
# print("# (1) 요소 내부에 있는 값 찾기")
# print("- {}는 {} 위치에 있습니다.".format(52, numbers.index(52)))
# print("# (2) 요소 내부에 없는 값 찾기")
# number = 10000
# try:
#     print("- {}는 {} 위치에 있습니다.".format(number, numbers.index(number)))
# except:
#     print("- 리스트 내부에 없는 값입니다.")
# print("--- 정상적으로 종료되었습니다. ---")

# 문제 3 -- 
# output = 10 + "개"   # 예외 => TypeError: unsupported operand type(s) for +: 'int' and 'str'
# int("안녕하세요")     # 예외 => ValueError: invalid literal for int() with base 10: '안녕하세요'
# cursor.close)   # 구문 오류 => SyntaxError: unmatched ')'
# [1,2,3,4,5][10]     # 예외 => IndexError: list index out of range

# ======================================
# ----- 06-2 예외 고급 -----
# ======================================
# 예외 객체 exception object (예외 정보)
# try: 예외가 발생할 가능성이 있는 구문
# except 예외의 종류 as 예외 객체를 활용할 변수 이름: 예외가 발생했을 때 실행할 구문

# 예제1 -- 예외 객체
# try:
#     number_input_a = int(input("정수 입력>> "))
#     print("원의 반지름:", number_input_a)
#     print("원의 둘레:", 2 * 3.14 * number_input_a)
#     print("원의 넓이:", 3.14 * number_input_a * number_input_a)
# except Exception as exception:
#     print("type(exception):", type(exception))  # type(exception): <class 'ValueError'>
#     print("exception:", exception)      # exception: invalid literal for int() with base 10: '안녕'

# 예제2 -- 여러가지 예외가 발생할 수 있는 코드
# list_number = [52,273,32,72,100]
# try:
#     number_input = int(input("정수입력>> "))    # 정수로변환 불가한값 입력시: ValueError, 리스트길이 넘는 인덱스 입력시: IndexError
#     print("{}번째 요소: {}".format(number_input, list_number[number_input]))
# except Exception as exception:
#     print("type(exception):", type(exception))
#     print("exception:",exception)

# 예제3 -- 예외 구분하기
# try: 예외가 발생할 가능성이 있는 구문
# except: 예외의 종류A: 예외A가 발생했을 때 실행할 구문
# except: 예외의 종류B: 예외B가 발생했을 때 실행할 구문
# list_number = [52,273,32,72,100]
# try:
#     number_input = int(input("정수입력>> "))
#     print("{}번째 요소: {}".format(number_input, list_number[number_input]))
# except ValueError:
#     print("정수를 입력해주세요.")
# except IndexError:
#     print("리스트의 인덱스를 벗어났어요.")

# 예제4 -- 예외 구문과 예외 객체
# list_number = [52,273,32,72,100]
# try:
#     number_input = int(input("정수 입력>> "))
#     print("{}번째 요소: {}".format(number_input, list_number[number_input]))
# except ValueError as exception:
#     print("정수를 입력해주세요.")
#     print("type(exception):", type(exception))
#     print("exception:", exception)
# except IndexError as exception:
#     print("리스트의 인덱스를 벗어났어요.")
#     print("type(exception):", type(exception))
#     print("exception:", exception)

# 예제5 -- 예외 처리를 했지만 예외를 못 잡는 경우
# list_number = [52,273,32,72,100]
# try:
#     number_input = int(input("정수 입력>> "))
#     print("{}번째 요소: {}".format(number_input, list_number[number_input]))
#     예외.발생해주세요()     # ←←←← 이 부분에서 잡지 않은 예외 발생
# except ValueError as exception:
#     print("정수를 입력해주세요.")
#     print("type(exception):", type(exception))
#     print("exception:", exception)
# except IndexError as exception:
#     print("리스트의 인덱스를 벗어났어요.")
#     print("type(exception):", type(exception))
#     print("exception:", exception)

# p389 -- 예제6 -- 모든 예외 잡기
# list_number = [52,273,32,72,100]
# try:
#     number_input = int(input("정수 입력>> "))
#     print("{}번째 요소: {}".format(number_input, list_number[number_input]))
#     예외.발생해주세요()
# except ValueError as exception:
#     print("정수를 입력해주세요.")
#     print(type(exception), exception)
# except IndexError as exception:
#     print("리스트의 인덱스를 입력해주세요.")
#     print(type(exception), exception)
# except Exception as exception:      # ValueError, IndexError가 아닌 예외가 발생했을 때 실행됨.
#     print("미리 파악하지 못한 예외가 발생했습니다.")
#     print(type(exception), exception)

# ======================================
# ----- 06-2 예외 고급 - raise 구문 : 강제 예외 발생시키기 -----
# ======================================
# raise구문 사용방법: raise 예외 객체

# 예제1 -- 아직 구현되지 않은 부분에서 강제로 예외 발생시키기
# number = input("정수입력>> ")
# number = int(number)
# if number > 0:
#     raise NotImplementedError
# else:
#     raise NotImplementedError

# ======================================
# ----- 06-2 예외 고급 - 좀더알아보기 -----
# ======================================
# 예제1 -- finally가 없을 경우의 코드
# def get_geometry_type(self, table_name, geo_col):
#     cursor = self.connection.cursor()
#     try:
#         cursor.execute('DESCRIBE %s' % self.connection.ops.quote_name(table_name))
#         for column, typ, null, key, default, extra in cursor.fetchall():
#             if column == geo_col:
#                 field_type = OGRGeomType(typ).django
#                 field_params = {}
#                 cursor.close()
#                 break
#     except:
#         cursor.close()
#     cursor.close()
# 예제2 -- finally 코드 사용하니 간결해짐
# def get_geometry_type(self, table_name, geo_col):
#     cursor = self.connection.cursor()
#     try:
#         cursor.execute('DESCRIBE %s' % self.connection.ops.quote_name(table_name))
#         for column, typ, null, key, default, extra in cursor.fetchall():
#             if column == geo_col:
#                 field_type = OGRGeomType(typ).django
#                 field_params = {}
#                 break
#     finally:
#         cursor.close()