x=0
def add(x):
    return x+x

# 자기자신에서(main.py에서) 실행될 때만 실행됨 => p0408_05.py에서 실행안됨
if __name__=="__main":
    print("입력된 값: ",x)

