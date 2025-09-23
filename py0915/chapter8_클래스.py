# ---------------------------------
# Chapter 08 클래스


# ======================================
# p460 ----- 08-1 클래스의 기본 -----
# ======================================
# 객체지향 프로그래밍언어 Object Oriented Programming : 객체를 우선으로 생각해서 프로그래밍함 (C를 제외한 모든 프로그래밍 언어)
# 클래스 class
# 객체 object : 속성과 메소드를 갖는 것, 속성을 가질 수 있는 모든 것

# 예제1 -- 객체 만들기
# students = [  # 학생 리스트 선언
#     {"name": "윤인성", "kor": 87, "math": 98, "eng": 88},
#     {"name": "연하진", "kor": 92, "math": 98, "eng": 96},
#     {"name": "구지연", "kor": 76, "math": 96, "eng": 94}
# ]
# print("이름","총점","평균",sep="\t")
# for student in students:
#     # 점수 총합, 평균 구함
#     score_sum = student["kor"] + student["math"] + student["eng"]
#     score_avg = score_sum / 3.0
#     print(student["name"], score_sum, f"{score_avg:.2f}", sep="\t")

# 예제2 -- 객체를 만드는 함수(1)
# def create_student(name, kor, math, eng):  # 딕셔너리 리턴하는 함수 선언
#     return {
#         "name": name,
#         "kor": kor,
#         "math": math,
#         "eng": eng
#     }
# students = [  # 학생 리스트 선언
#     create_student("윤인성",87,98,88),
#     create_student("연하진",92,98,96),
#     create_student("구지연",76,96,94)
# ]
# print("이름","총점","평균",sep="\t")  # 학생 한 명씩 반복
# for student in students:
#     # 점수 총합, 평균 구함
#     score_sum = student["kor"] + student["math"] + student["eng"]
#     score_avg = score_sum / 3.0
#     print(student["name"], score_sum, f"{score_avg:.2f}",  sep="\t")
    
# 예제3 -- 객체를 처리하는 함수(2)
# def create_student(name, kor, math, eng):  # 딕셔너리 리턴하는 함수 선언
#     return {
#         "name": name,
#         "kor": kor,
#         "math": math,
#         "eng": eng
#     }
# def student_get_sum(student):   # 학생 처리하는 함수 선언
#     return student["kor"] + student["math"] + student["eng"]
# def student_get_avg(student):
#     return student_get_sum(student) / 3.0
# def student_to_string(student):
#     return "{}\t{}\t{:.2f}".format(
#         student["name"],
#         student_get_sum(student),
#         student_get_avg(student)
#     )
# students = [  # 학생 리스트 선언
#     create_student("윤인성",87,98,88),
#     create_student("연하진",92,98,96),
#     create_student("구지연",76,96,94)
# ]
# print("이름", "총점", "평균", sep="\t")
# for student in students:
#     print(student_to_string(student))