# # 파일 입출력
# # 표준입력장치 → input() → 파이썬 프로그램 → print() → 표준출력장치
# # 파일        → read()  → 파이썬 프로그램 → write()  → 파일
# #              readline()               → writelines()
# #              readlines()
# #____________________________________
# 메모장: 문서를 저장하는 곳(문자열 타입)

# # 파일입출력 기본과정:
# # 1) 파일 열기 - 3가지모드(r:읽기모드, w:쓰기모드, a:추가모드, b:이진파일-복사할때 씀)
# # 2) 파일 읽기/쓰기
# # 3) 파일 닫기
# #____________________________________
# # 1) 파일 열기
# f=open("a.txt","r")  # 읽기모드
# f=open("a.txt","w")  # 쓰기모드
# f=open("a.txt","a")  # 추가모드
# #____________________________________


# ◆◆◆ 파일 열기 - r 읽기모드


# # Q1. news.txt 파일 출력하시오.
# # f=open("py0404/news.txt","r",....)
# f=open("py0404/news.txt","r",encoding="utf-8")    # utf-8: 전 세계 대부분의 문자를 표현할 수 있는 유니코드 인코딩 방식
# for line in f:
#     print(line.strip())
# f.close()

# #--------------
# # 파일 읽어오기 - 절대경로
# # f=open("C:/workspace/python/a.txt","r",encoding="utf-8")  # 폴더 안에 없는 경우
# f=open("/py0404/b.txt",encoding="utf-8")                    # 폴더 안에 있는 경우    
# for line in f:
#     print(line.strip())
# f.close()  # 꼭 하기

# while True:  # 3줄
#     line=f.readline()
#     if not line: break
#     print(line.strip())
# f.close()
# #--------------

# # 파일 읽기 - readlines() (모두 읽어오기_시간 오래 걸릴 수 있음)
# f=open("a.txt","r",encoding="utf-8")
# lines=f.readlines()  # 모두 읽어오기 (lines=리스트 개념)
# for line in lines:
#     print(line.strip())
# f.close()

# # 파일 읽기 - r (1줄 읽기)
# f=open("a.txt","r",encoding="utf-8")
# print(type(f))
# 모든 줄을 실행 - for문을 사용
# for line in f:
#     print(line.strip())  # .strip 공백 제거
# f.close()




