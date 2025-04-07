# 파이썬 - 파일구성 : 다른 타입형태 넣을수 있다는 장점

# 변수 -> 배열(같은타입) -> 다른타입(구조체) | -> 객체(클래스)-변수,함수
# * 객체지향언어 - 고급언어 

# 클래스 장점
# - 변수,함수 모두 포함
# - 변수에 대한 값을 확인,비교
# - 캡슐화 : 변수에 직접 접근을 막을수 있음.

# class 첫글자 대문자사용, 강제 아님(권장사항)
# 설계도.
class Stu:
    # 생성자 - 클래스가 선언될때 데이터를 받아서 변수에 저장함수
    def __init__(self,no,name,kor,eng,math,total,avg,rank):
        self.no = no #class안에 변수가 선언이 됨.
        self.name = name
        if kor>=0 and kor<=100:
            self.kor = kor
        self.__eng = eng
        self.math = math
        self.total = total
        self.avg = avg
        self.rank = rank
        
    def print(self):
        print(self.no,self.name,self.__eng)    

# stu = [1,"홍길동",100,100,100,300,100.0,1]        
s = Stu(1,"홍길동",200,100,100,300,100.0,1)
s.__eng = 200
print(s.__eng)
print(s.print())


# 클래스선언후, 변수선언을 해서 사용가능
# class Stu:
#     pass

# s = Stu() # 클래스선언
# s.no = 1  # 변수선언
# s.name = "홍길동" #변수선언
# s.kor = 100      #변수선언





stu = [1,"홍길동",100,100,100,300,100.0,1]
while True:
    stu[2] = 300
    print("1.학생출력")
    choice = int(input("원하는 번호를 입력하세요.>> "))
    if choice == 1:
        print(stu)
