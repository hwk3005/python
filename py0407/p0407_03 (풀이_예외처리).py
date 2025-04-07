print(1)
print(2)
raise NotImplementedError  # 프로그램 구현이 아직 진행이 안되었음.
print(3)


# try:          # 프로그램 구현부분
#     print(1)
#     print(2)
#     # raise NotImplementedError  # 예외를 강제로 발생시킴
#     raise ZeroDivisionError
#     # choice = int(input("숫자를 입력하세요.>> ")) #문자입력
#     print(3)
#     print(4)
# except Exception as e:      # 에러가 났을때 실행
#     print(e)
#     print(5)
# else:        # 에러가 나지 않았을때 실행
#     print(6)
# finally:     # 에러시, 에러가 나지 않았을때 모두 실행
#     print(7)  



# try:          # 프로그램 구현부분
#     print(1)
#     print(2)
#     choice = int(input("숫자를 입력하세요.>> ")) #문자입력
#     print(3)
#     print(4)
# except:      # 에러가 났을때 실행
#     print(5)
# else:        # 에러가 나지 않았을때 실행
#     print(6)
# finally:     # 에러시, 에러가 나지 않았을때 모두 실행
#     print(7)            




# try:
#     num = int(input("원의 반지름을 입력하세요.>> "))
#     print("원의 넓이 : ",3.14 * num**2) 
# except Exception as e:
#     print(e)
# else: # try구문에 에러가 없을시 실행
#     pass  
        



# a_list = ["52","273","32","파이썬","103"]

# list_number = []
# 숫자로 변환되는 것만 list_number 저장하시오.
# if문을 사용, 예외처리해서 사용

# 예외처리사용 - a_list변환
# for a in a_list:
#     try: 
#         list_number.append(int(a))
#     except Exception as e: print(e)    

# print("리스트 출력 : ",list_number)   
         
# # if문사용 - a_list변환
# for a in a_list:
#     if a.isdigit():
#         list_number.append(int(a))
#     else:
#         print("숫자가 아님 : ",a)

# print("리스트 출력 : ",list_number)            