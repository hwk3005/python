class Student:  # Student
    count=1  # 클래스 변수
    def __init__(self,name,kor,eng,math):  # 생성자함수
        self.no=Student.count
        self.name=name
        self.kor=kor
        self.eng=eng
        self.math=math
        self.total=kor+eng+math
        self.avg=(kor+eng+math)/3
        self.rank=0
        Student.count+=1
    def __str__(self):  # 특별함수
         return f"{self.no},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg:.2f},{self.rank}"

class Students:  # Students
    def __init__(self):
        self.students=[]
    def add(self,s):
        self.students.append(s)
    def __str__(self):
        title=['번호','이름','국어','영어','수학','합계','평균','등수']
        print("{},{},{},{},{},{},{},{}".format(*title))
        print("-"*60)
        for s in self.students:
            print(s.no,s.name,s.kor,s.eng,s.math,s.total,s.avg,s.rank)
        return ""
        