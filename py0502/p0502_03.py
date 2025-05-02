### 학생성적프로그램에서 1명 학생을 등록해보세요.
from stuConn import *
conn = connections()
### 직접입력
name = input("이름을 입력하세요.>> ")
kor = int(input("국어점수를 입력하세요.>> "))
eng = int(input("영어점수를 입력하세요.>> "))
math = int(input("수학점수를 입력하세요.>> "))
total = kor+eng+math
avg = total/3

#### insert - 1개 저장
cursor = conn.cursor()
query = "insert into stuscore values(\
stuscore_seq.nextval,:name1,:kor1,:eng1,:math1,:total1,:avg1,0)"
cursor.execute(query,name1=name,kor1=kor,eng1=eng,math1=math,total1=total,avg1=avg)
conn.commit()
print(name,"학생 성적이 저장되었습니다.")
print()
