import oracledb

# db연결
def connections():
    try: conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
    except Exception as e: print(e)
    return conn
## 학생성적입력
def stuInsert():
    ## 1. 이름,국어,영어,수학점수 입력 -> 합계,평균, 등수,등급처리
    name = input("이름을 입력하세요.>> ")
    kor = int(input("국어점수를 입력하세요.>> "))
    eng = int(input("영어점수를 입력하세요.>> "))
    math = int(input("수학점수를 입력하세요.>> "))
    total = kor+eng+math
    avg = total/3
    
    conn = connections()
    cursor = conn.cursor()
    ## insert
    sql = "insert into stuscore values \
        (stuscore_seq.nextval,:name,:kor,:eng,:math,:total,:avg,0,'F')"
    cursor.execute(sql,name=name,kor=kor,eng=eng,math=math,total=total,avg=avg)
    conn.commit()
    print(f"{name}학생 성적이 저장되었습니다.")
    print()
    cursor.close()
    conn.close()
    

## 학생전체출력
def stuAllSelect(sql='select * from stuscore'):
    conn = connections()
    cursor = conn.cursor()
    ### select 
    cursor.execute(sql)
    rows = cursor.fetchall()
    for r in rows:
        print(r)
    cursor.close()    
    conn.close() 

## 학생성적검색
def stuSearch():
    search = input("검색하려는 이름을 입력하세요.>> ")
    
    conn = connections()
    cursor = conn.cursor()
    ## select
    sql = "select * from stuscore where name like '%'||:search||'%'"
    cursor.execute(sql,search=search)
    rows = cursor.fetchall()
    if len(rows)>0:
        for r in rows:
            print(r)
    else:
        print(f"찾고자 하는 {search} 학생이 없습니다. 다시 입력하세요.")        
    cursor.close()    
    conn.close() 
    
## 정렬
def stuSort():
    print("[ 학생성적 정렬 ]")
    print("1. 이름정렬")
    print("2. 성적정렬")
    print("3. 국어정렬")
    print("4. 영어정렬")
    print("5. 수학정렬")
    print("9. 번호정렬")
    choice = input("원하는 번호를 입력하세요.>> ")
    if choice == "1": sorting('이름','name')
    elif choice == "2": sorting('성적','rank')
    elif choice == "3": sorting("국어",'kor')
    elif choice == "4": sorting("영어",'eng')
    elif choice == "5": sorting("수학",'math')
    elif choice == "9": sorting("번호",'sno')
        


## 순차정렬,역순정렬
def sorting(sName,sName2):
    print(f"1. {sName}순차정렬")
    print(f"2. {sName}역순정렬")
    choice = input("원하는 번호를 입력하세요.>> ")
    if choice == "1": sql = f"select * from stuscore order by {sName2}"
    else: sql = f"select * from stuscore order by {sName2} desc"
    stuAllSelect(sql)        

## 등수처리 - 1,2,...
def rankUpdate():
    conn = connections()
    cursor = conn.cursor()
    ### update
    sql = "update stuscore a set rank = (\
    select ranks from\
    (select sno,rank() over(order by total desc) ranks from stuscore) b\
    where a.sno = b.sno)"
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

## 등급처리 - A,B,C,D,F
def gradeUpdate():
    conn = connections()
    cursor = conn.cursor()
    ### update
    sql = "update stuscore a set sgrade = (\
            select grade from (\
            select sno,avg,grade from stuscore,scoregrade\
            where avg between minscore and maxscore\
            ) b where a.sno = b.sno )"
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

