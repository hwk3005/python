class Student:  # 대문자-클래스라고 생각하면 됨.
    # 인스턴스 변수 - 객체선언 시 각각 변수들이 존재: 공용으로 사용안됨.
    # no=1
    # name=""  # 인스턴스 변수
    count=1    # 클래스 변수 - 모든 객체가 공용으로 사용하는 변수

    # 생성자함수
    def __init__(self,name,kor,eng,math):
        self.no=Student.count       # 인스턴스 변수
        self.name=name
        self.kor=kor
        self.eng=eng
        self.math=math
        self.total=kor+eng+math
        self.avg=(kor+eng+math)/3
        self.rank=0
        Student.count+=1  # 1증가 (객체선언 할때마다)
        
    def __str__(self):  # 특별함수
        return f"{self.no},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg:.2f},{self.rank}"

class Students:
    def __init__(self):
        self.students=[]
        
    def add(self,s):
        self.students.append(s)

    def __str__(self):  # 리턴return이 무조건 문자열을 해줘야 함.
        for s in self.students:
            print(s.no,s.name,s.kor,s.eng,s.math,s.total,s.avg,s.rank)
        return ""
ss=Students()
s=Student("홍길동",100,100,99)
s2=Student("유관순",90,90,91)
s3=Student("이순신",80,80,89)
ss.add(s)
ss.add(s2)
ss.add(s3)
print(ss)

      
# # 매개변수가 있는 생성자를 활용해서 데이터 입력
# s=Student("홍길동",100,100,99)  # 매개변수가 있는 생성자 객체선언
# print(s.no,s.name,s.kor,s.eng,s.math,Student.count)  # 2
# s2=Student("유관순",99,99,98)
# print(s2.no,s2.name,s2.kor,s2.eng,s2.math,Student.count)  # 3
# print(s.no,s.name,s.kor,s.eng,s.math,Student.count)  # 3
# s3=Student("이순신",90,90,91)
# print(s3.no,s3.name,s3.kor,s3.eng,s3.math,Student.count)  # 4
# print(s.no,s.name,s.kor,s.eng,s.math,Student.count)  # 4
# print(s.no,s.name,s.kor,s.eng,s.math,Student.count)  # 4



# a_list=[1,2]

# # 기본생성자를 가지고 객체선언 후 데이터 입력 
# s=Student()  # 기본생성자
# s.name="홍길동"
# print(s.no,s.name)

# s2=Student()
# s2.no=2
# s2.name="이순신"
# print(s2.no, s2.name)

