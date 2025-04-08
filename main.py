# main.py 하위폴더에 파일이 존재하면
# 폴더이름.파일명
# from stuProject.stuModule import *   # 폴더가 다르면 앞에 폴더이름을 붙여줌.
import stuProject.stuModule as stum

b=stum.Student("홍길동",100,100,100)
print(b)

