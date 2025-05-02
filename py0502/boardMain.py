## 게시글 등록 작성

## 1. db연결
## 2. 게시판 글쓰기
## 3. 파일첨부 등록
## 4. 시퀀스 번호 생성
## 5. 파일 리스트 생성
## 6. db에 게시글 저장
## 7. db에 파일첨부 여러개저장
## 8. 프로그램 종료
#-----------------------------------------------

## 게시글 등록 작성
from stuConn import *

## 1. db연결
conn=connections()

## 2. 게시판 글쓰기
title=input("게시글 제목을 입력하세요.>> ")
content=input("게시글 내용을 입력하세요.>> ")

## 3. 파일첨부 등록
bname=[]
count=0
while True:
    temp=input(f"{count+1}번 첨부할 파일을 입력하세요.(0.종료)>> ")
    if temp=='0': break
    bname.append(temp)
    count += 1
    
## 4. 시퀀스 번호 생성
cursor=conn.cursor()
query="select board_seq.nextval from dual"
cursor.execute(query)
bno=cursor.fetchone()[0]
print("시퀀스번호 생성: ",bno)

## 5. 파일 리스트 생성
bfile=[]
for b in bname: bfile.append([bno,b])

## 6. db에 게시글 저장
query="insert into board values (:bno,:btitle,:bcontent,'aaa',\
        :bno,0,0,0,sysdate)"
cursor.execute(query,bno=bno, btitle=title,bcontent=content)
conn.commit()

## 7. db에 파일첨부 여러개저장
query="insert into bfile values (:1,:2)"
cursor.executemany(query,bfile)
conn.commit()
conn.close()

## 8. 프로그램 종료
print(bfile)
print("프로그램을 종료합니다.")
