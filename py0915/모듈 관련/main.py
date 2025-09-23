# import test_module as test
# radius = test.number_input()  # 함수 호출
# print(test.get_circumference(radius))
# print(test.get_circle_area(radius))

# --------------------------------

# import test_module
# print("# 메인의 __name__ 출력하기")
# print(__name__)
# print()

# --------------------------------

# import test_module as test
# radius = test.number_input()
# print(test.get_circumference(radius))
# print(test.get_circle_area(radius))

# --------------------------------
# p441 -- 쉬운 모듈만들기
# import test_module as test
# radius = test.number_input()
# print(test.get_circumference(radius))
# print(test.get_circle_area(radius))
# --
# import test_module as test
# radius = test.number_input()
# print(test.get_circumference(radius))
# print(test.get_circle_area(radius))
# --
# import test_module as test
# radius = test.number_input()
# print(test.circumference(radius))
# print(test.circle_area(radius))

# --------------------------------
# p442 -- 모듈 이름을 출력하는 모듈 만들기
# import test_module
# print("# 메인의 __name__ 출력하기")
# print(__name__)  # main일 경우 __name__ ==> __main__

# --------------------------------
# p443~445 -- 모듈 활용하기, 엔트리 포인트를 확인하는 모듈 만들기
# import test_module as test
# radius = test.number_input()
# if __name__ == "__main__":
#     print(test.get_circumference(radius))
#     print(test.get_circle_area(radius))

# --------------------------------
# p446 -- 패키지 만들기 (1)
import test_package.test_module_a as a
import test_package.test_module_b as b
print(a.variable_a)
print(b.variable_b)
