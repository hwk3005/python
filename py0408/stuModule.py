class Student:
    # 인스턴스 변수 - 객체선언시 각각 변수들이 존재 : 공용으로 사용안됨.
    # no = 1 
    # name = "" # 인스턴스 변수
    count = 1   # 클래스변수 - 모든 객체가 공용으로 사용하는 변수
        
    # 생성자함수
    def __init__(self,name,kor,eng,math):
        self.no = Student.count       # 인스턴스변수
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math 
        self.avg = (kor+eng+math)/3  
        self.rank = 0 
        Student.count += 1           # 1증가
    
    def stu_total(self):
        self.total=self.kor + self.eng + self.math  # (위에 self.kor/eng/math 가져와서 self.total로 다시 돌려놓음)
    def stu_avg(self):
        self.avg=self.total/3
    
    def __le__(self,s):
        return (self.total<=s.total)
    def __ge__(self,s):
        return (self.total>=s.total)
    
    def __eq__(self,s):     # 다른 객체 1개를 매개변수로 전달받음.
        return(self.total == s.total)  # 같으면 True, 다르면 False
    
    def __str__(self):
        return f"""{self.no},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg:.2f},{self.rank}"""

class Students:
    def __init__(self):
        self.students = []  
    
    def add(self,s):
        self.students.append(s)    
  
    def __str__(self):  # 리턴이 무조건 문자열을 해줘야 함.
        
        for s in self.students:
            print(s.no,s.name,s.kor,s.eng,s.math,s.total,s.avg,s.rank)
        return "" 

      
