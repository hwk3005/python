### 1. 로또 프로그램
import random
# 6개 숫자 랜덤 번호 생성
# 6개 입력한 번호 생성
# 당첨번호 확인
# 출력


lotto=[i+1 for i in range(45)]  # 로또 랜덤 번호
lotto2=[i+1 for i in range(45)]  # 로또 순차적 번호 출력

# choice==1 함수선언
def lotto_mix():
    random.shuffle(lotto)
    
lotto_mix()
while True:
    print(" "*5,"[ 로또 프로그램 ]")
    print("-"*30)
    print("1. 로또프로그램 재실행")
    print("2. 로또번호 입력")
    print("3. 로또번호 당첨확인")
    print("4. 로또리스트 모두 확인")
    print("5. 내가 입력한 로또번호 확인")
    print("0. 프로그램 종료")
    print("-"*30)
    choice=int(input("원하는 번호를 입력하세요.>> "))
    
    if choice==1:
        lotto_mix()
        
    elif choice==2:
        print(" "*15,"[ 2. 로또번호 입력 ]")
        print("-"*50)
        # 로또 번호 순번출력부분-------------------
        for i in range(45):
            if i==0: pass
            elif i%7==0:
                print()
            print(lotto2[i],end="\t")
        print()
        # 로또번호 입력문구------------------------
        choice=int(input("로또번호를 입력하세요.(0.이전화면 이동)>> "))
        if choice==0: break
        # 0미만 or 45초과 숫자 입력 시 재실행하라는 문구----------
        if choice<0 or choice>45:
            print(f"{choice}번 번호는 없는 번호입니다. 다시 확인해주세요.")
            continue  # 재실행 (챗gpt: 불필요할 가능성 있음)
        # 해당로또번호 X표시부분--------------------
        
        
        
        
    elif choice==3:
        pass
    elif choice==4:
        pass
    elif choice==5:
        pass
    else:
        print("[ 0. 프로그램 종료 ]")
        break
