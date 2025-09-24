# ---------------------------------
# Chapter 07 모듈


# ======================================
# p401 ----- 07-1 표준 모듈 ----- math 모듈
# ======================================
# 파이썬 - 모듈 module 기능을 활용해 코드 분리 및 공유함.
# 모듈: 여러 변수 + 함수 가지고 있는 집합체 (표준모듈(기본내장됨) + 외부모듈(외부인이 만들어 공개한 모듈))
# import 모듈 이름

# 예제1 -- math 모듈
# import math
# print(math.sin(1))  # 사인
# print(math.cos(1))  # 코사인
# print(math.tan(1))  # 탄젠트
# print(math.floor(2.5)) # 내림
# print(math.ceil(2.5))  # 올림
# print(math.log(x, base)) # 로그값
# print(round(1.5))  # 정수부분이 홀수인 경우: .5일때 소수점 반올림함
# print(round(4.5))  # 정수부분이 짝수인 경우: .5일때 소수점 버림

# 예제2 -- from 구문
# from 모듈이름 import 가져오고 싶은 변수 또는 함수
# from math import sin,cos,tan,floor,ceil
# print(sin(1))  # 함수 앞에 모듈이름. 안 붙여도 됨.
# print(cos(1))
# print(tan(1))
# print(ceil(1.4))
# print(floor(4.8))

# 예제3 -- as 구문
# import 모듈 as 사용하고 싶은 식별자
# import math as m
# print(m.sin(1))
# print(m.cos(1))
# print(m.tan(1))
# print(m.ceil(1.4))
# print(m.floor(4.8))

# from math import *
# import math as m

# ======================================
# p406 ----- 07-1 표준 모듈 ----- random 모듈
# ======================================
# 예제1 --
# import random
# from random import random, uniform, randrange, choice, shuffle, sample
# print("random():", random.random())  # 0.0 <= x < 1.0 - float
# print("uniform(10,20):", random.uniform(10,20))  # min, max - float
# print("randrange(10):", random.randrange(10))  # max - int
# print("randrange(1,10):", random.randrange(1,10))  # min, max - int
# print("choice([1,2,3,4,5]):", random.choice([1,2,3,4,5]))  # 리스트 내부요소 랜덤 선택
# print("shuffle([1,2,3,4,5]):", random.shuffle([1,2,3,4,5]))  # 리스트 내부요소 랜덤 섞음
# print("sample([1,2,3,4,5], k=2):", random.sample([1,2,3,4,5], k=2))  # 리스트 요소 중 k개 뽑음

# ======================================
# p408 ----- 07-1 표준 모듈 ----- sys 모듈 : 시스템과 관련된 정보 가지고 있는 모듈, 명령 매개변수 받을 때 많이 사용함.
# ======================================
# 예제1 --
# import sys
# print("sys.argv:", sys.argv)  # 명령 매개변수 출력  # sys.argv: ['c:\\workspace\\python\\py0915\\chapter7_모듈.py']
# # 컴퓨터 환경과 관련된 정보 출력
# print("sys.getwindowsversion():", sys.getwindowsversion())  # sys.getwindowsversion(): sys.getwindowsversion(major=10, minor=0, build=19045, platform=2, service_pack='')
# print("copyright:", sys.copyright)
# print("sys.version:", sys.version)
# sys.exit()

# ======================================
# p410 ----- 07-1 표준 모듈 ----- os 모듈 : 운영체제 관련 기능 가진 모듈, 새 폴더 생성 or 폴더내부 파일목록 조회 등
# ======================================
# 예제1 --
# import os
# print("현재 운영체제:", os.name)
# print("현재 폴더:", os.getcwd())
# print("현재 폴더 내부 요소:", os.listdir())
# os.mkdir("hello")  # 폴더 생성
# os.rmdir("hello")  # 폴더 삭제
# with open("original.txt","w") as file:
#     file.write("hello")   # 파일 생성
# os.rename("original.txt", "new.txt")  # 파일 이름변경
# os.remove("new.txt")  # 파일 제거
# os.unlink("new.txt")  # 파일 제거
# os.system("dir")      # 시스템 명령어 실행 (cmd에서 dir 입력결과와 동일)
# # os.system() 함수 위험함. 잘못 실행할 경우 컴퓨터 모든 것 삭제됨.

# ======================================
# p412 ----- 07-1 표준 모듈 ----- datetime 모듈 - 날짜 위주 : strftime(), timedelta(), replace()
# ======================================
# 예제1 -- datetime 모듈
# import datetime
# now = datetime.datetime.now()
# print(now.year, "년")
# print(now.month, "월")
# print(now.day, "일")
# print(now.hour, "시")
# print(now.minute, "분")
# print(now.second, "초")
# print("# 시간을 포맷에 맞춰 출력하기")
# strftime = string format time  형식 지정해서 사용가능
# output_a = now.strftime("%Y.%m.%d %H:%M:%S")
# output_b = "{}년 {}월 {}일 {}시 {}분 {}초".format(
#     now.year,\
#     now.month,\
#     now.day,\
#     now.hour,\
#     now.minute,\
#     now.second )
# output_c = now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초")
# print(output_a)
# print(output_b)
# print(output_c)

# 예제2 -- 시간 처리하기
# import datetime 
# now = datetime.datetime.now()
# 특정 시간 이후의 시간 구하기 - timedelta()
# print("# datetime.timedelta로 시간 더하기")
# after = now + datetime.timedelta(\
#     weeks=1,\
#     days=1,\
#     hours=1,\
#     minutes=1,\
#     seconds=1)
# print(after.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))
# 특정 시간 요소 교체하기 - replace()
# print("# now.replace()로 1년 더하기")
# output = now.replace(year=(now.year+1))
# print(output.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))

# ======================================
# p414 ----- 07-1 표준 모듈 ----- time 모듈 - 시간 위주 : time.sleep()
# ======================================
# 예제1 --
# import time
# print("지금부터 5초 동안 정지합니다.")
# time.sleep(5)
# print("프로그램을 종료합니다.")  # 5초 동안 정지한 이후에 출력됨.

# ======================================
# p415 ----- 07-1 표준 모듈 ----- urllib 모듈 - url 다루는 라이브러리 : urlopen() / Uniform Resource Locator
# ======================================
# 예제1 -- 
# from urllib import request
# target = request.urlopen("https://google.com")
# output = target.read()
# print(output)
#b : 바이너리 데이터 binary data
#b'<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="ko"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><title>Google</title><script nonce="QbGeKEMobEhK4ZhLar-s9A">(function(){var _g={kEI:\'mLzQaOmSFIex0PEPkcqBgA0\',kEXPI:\'0,202854,2,34,16,11,21,4037107,48791,30022,16105,344796,219813,70231,524216

# ======================================
# p417 ----- 좀더알아보기 ----- operator 모듈 : itemgetter() 특정요소를 추출하는 함수를 만드는 함수
# ======================================
# 예제1 -- 
# from operator import itemgetter
# books = [{
#     "제목": "혼자 공부하는 파이썬",
#     "가격": 18000
# }, {
#     "제목": "혼자 공부하는 머신러닝 + 딥러닝",
#     "가격": 26000
# }, {
#     "제목": "혼자 공부하는 자바스크립트",
#     "가격": 24000
# }]
# print(min(books, key=itemgetter("가격")))
# print(max(books, key=itemgetter("가격")))

# ======================================
# p420 ----- 마무리 확인문제 -----
# ======================================
# 문제3 --
# import os
# output = os.listdir(".")
# print("os.listdir():", output)
# print("# 폴더와 파일 구분하기")
# for path in output:
#     if os.path.isdir(path):
#         print("폴더:",path)
#     else:
#         print("파일:",path)

# 문제3-1 --
# import os
# def read_folder(path):
#     output = os.listdir(path)
#     for item in output:
#         if os.path.isdir(item):
#             read_folder(item)
#         else:
#             print("파일:",item)
# read_folder(".")

# chat GPT 보완 버전 --
# import os
# def read_folder(path):
#     output = os.listdir(path)       # 현재 폴더 안 항목 목록
#     for item in output:
#         full_path = os.path.join(path, item)  # 전체 경로 만들기
#         if os.path.isdir(full_path):          # 폴더인지 확인
#             read_folder(full_path)            # 재귀적으로 탐색
#         else:
#             print("파일:", full_path)

# # 현재 폴더부터 탐색 시작
# read_folder(".")


# ======================================
# p425 ----- 07-2 외부 모듈 ----- Beautiful Soup 모듈 : 웹페이지 분석모듈
# ======================================
# pip install : 외부 모듈을 설치할 때 사용하는 명령어
# 예제1 -- Beautiful Soup 모듈로 날씨 가져오기
# from urllib import request
# from bs4 import BeautifulSoup
# # urlopen() 함수로 기상청의 전국날씨 읽기
# target = request.urlopen("https://www.weather.go.kr/w/weather/forecast/mid-term.do?stnId1=108")
# # BeautifulSoup 사용해 웹페이지 분석하기
# soup = BeautifulSoup(target, "html.parser")
# # location 태그 찾기
# for location in soup.select("location"):
#     print("도시:", location.select_one("city").string)
#     print("날씨:", location.select_one("wf").string)
#     print("최저기온:", location.select_one("tmn").string)
#     print("최고기온:", location.select_one("tmx").string)

# ======================================
# p429 ----- 07-2 외부 모듈 ----- Flask 모듈 (플라스크) : 작은 기능만을 제공하는 웹개발 프레임워크 (Django 다양한 기능 제공)
# ======================================
# 예제1 -- Flask 모듈 사용하기
# from flask import Flask
# app = Flask(__name__)
# @app.route("/")  # 데코레이터 decorator
# def hello():
#     return "<h1>Hello World!</h1>"

# 예제2 -- Beautiful Soup 스크레이핑 실행하기
# 모듈 읽어 들이기
# from flask import Flask
# from urllib import request
# from bs4 import BeautifulSoup
# # 웹서버 생성
# app = Flask(__name__)
# @app.route("/")
# def hello():
#     # urlopen() 함수로 기상청의 전국날씨 읽기
#     target = request.urlopen("https://www.weather.go.kr/w/weather/forecast/mid-term.do")
#     # BeautifulSoup 사용해 웹페이지 분석하기
#     soup = BeautifulSoup(target, "html.parser")
#     # location 태그 찾기
#     output = ""
#     for location in soup.select("location"):
#         print(location)
        # 내부의 city, wf, tmn, tmx 태그 찾아 출력하기
    #     output += "<h3>{}</h3>".format(location.select_one("city").string)
    #     output += "날씨: {}<br/>".format(location.select_one("wf").string)
    #     output += "최저/최고 기온: {}/{}".format(\
    #         location.select_one("tmn").string,\
    #         location.select_one("tmx").string )
    #     output += "<hr/>"
    # return output
    
# ======================================
# p432 ----- 07-2 외부 모듈 ----- 라이브러리, 프레임워크
# ======================================
# 라이브러리 library : 정상적인 제어를 하는 모듈
# 프레임워크 framework : 제어 역전이 발생하는 모듈 (모듈이 개발자가 작성한 코드를 실행하는 형태의 모듈(제어역전됨))

# 예제1 -- 라이브러리
# from math import sin, cos, tan, floor, ceil
# print("sin(1):", sin(1))
# print("cos(1):", cos(1))
# print("tan(1):", tan(1))
# print("floor(2.5):", floor(2.5))
# print("ceil(2.5):", ceil(2.5))

# 예제2 -- 프레임워크
# from flask import Flask
# app = Flask(__name__)
# @app.route("/")
# def hello():
#     return "<h1>Hello World!</h1>"

# ======================================
# p435 ----- 좀더알아보기 ----- 함수 데코레이터 : @로 시작하는 구문
# ======================================
# 예제1 -- 함수 데코레이터의 기본
# def test(function):
#     def wrapper():
#         print("인사가 시작되었습니다.")
#         function()
#         print("인사가 종료되었습니다.")
#     return wrapper
# @test
# def hello():
#     print("hello")
# hello()

# 예제2 -- (챗gpt) 함수 실행 전에 날짜와 시간을 찍는 데코레이터
# import datetime
# def log_time(function):
#     def wrapper():
#         now = datetime.datetime.now()
#         print(now.strftime("[%Y-%m-%d %H:%M:%S] 함수를 실행합니다."))
#         function()
#     return wrapper

# @log_time
# def hello():
#     print("안녕~")
# hello()

# ======================================
# p440 ----- 07-3 모듈 만들기 ----- 함수 데코레이터 : @로 시작하는 구문
# ======================================
# 예제1 -- 쉬운 모듈 만들기
# test_module.py ,  main.py 파일 참고

# ======================================
# p442 ----- 07-3 모듈 만들기 ----- __name__ == "__main__"
# ======================================
# 엔트리 포인트(entry point) or 메인(main) : 프로그램의 진입점
# test_module.py ,  main.py 파일 참고
# 예제1 -- 모듈 이름을 출력하는 모듈 만들기
# 예제2 -- 모듈 활용하기
# 예제3 -- 엔트리 포인트를 확인하는 모듈 만들기

# 모듈  # import, from, as 구문
# - 표준모듈: math, random, sys, os, datetime, time, urllib
# - 예) import math as m / from math import sin, cos, tan
# - 외부모듈: BeautifulSoup, Flask, 라이브러리, 프레임워크

# p445 -- 패키지 package : 모듈이 모여서 구조를 이룬 것
# pip (Python Package Index) : 패키지 관리 시스템 Package Management System

# ======================================
# p449 ----- 좀더알아보기 : 텍스트 데이터, 바이너리 데이터 -----
# ======================================
# 파일 - 크게 "텍스트 데이터 text data / 바이너리 데이터 binary data" 구분
# 텍스트 데이터 : 쉽게 읽을 수 있음, 쉽게 편집 가능 (입력해왔던 모든 코드가 텍스트 데이터)
# 바이너리 데이터 : 텍스트 에디터로 열었을 때 의미를 이해할 수 없는 데이터
#  ㄴ 대표적 예: 이미지, 동영상 (-> 텍스트 데이터로 표현불가)

# << 비교 >> 
# 비교 항목     텍스트 데이터                         바이너리 데이터
# 구분 방법     텍스트 에디터로 열었을 때 읽을 수 o      텍스트 에디터로 열어도 읽을 수 x 
# 장점         사람이 쉽게 읽을 수 o, 쉽게 편집가능     용량 적음
# 단점         용량 큼                              사람이 쉽게 읽을 수 x, 에디터로 편집불가

# 인코딩 encoding : 텍스트 데이터를 맞춰서 읽기 쉬운 글자로 변환, 바이너리 데이터 읽어서 이미지로 변환하는 것
#  ㄴ 텍스트데이터 - ASCII, UTF-8, UTF-16, EUC-KR, Shift-JIS 등
#  ㄴ 바이너리데이터 - JPEG, PNG, GIF 등
# 디코딩 deconding : 인코딩된 데이터를 반대로 돌리는 것

# 예제1 -- 이미지 읽어 들이고 저장하기
# import ssl
# from urllib import request
# # SSL 인증 무시 컨텍스트 생성
# context = ssl._create_unverified_context()
# target = request.urlopen("https://www.hanbit.co.kr/images/common/logo_hanbit.png", context=context)
# output = target.read()
# print(output)
# # write binary(바이너리 쓰기) 모드로
# file = open("output.png","wb")  # wb: 바이너리 사용시 wb, 텍스트는 w (str타입)
# file.write(output)
# file.close()

