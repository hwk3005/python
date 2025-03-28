# 조건문  if / elif(추가조건) / else
# 3가지 조건
# 음수, 0, 양수

num=int(input("숫자를 입력하세요: "))
if num>0:
    print("양수입니다.")
elif num==0:
    print("0입니다.")
else:
    print("음수입니다.")


# Q1. 시험성적을 입력받아
#   Q1-1. 60점 이상이면 합격, 60점 미만이면 불합격 출력하시오.
test=int(input("시험성적을 입력하시오: "))
if test>=60:
    print("합격")
else:
    print("불합격")

#   Q1-2. 70점 이상 합격, 69~60점 재시험, 60점 미만 불합격
test2=int(input("시험성적을 입력하시오: "))
if test2>=70:
    print("합격")
elif test2>=60:
    print("재시험")
else:
    print("불합격")

#   Q1-3. 90점이상 A, 80점이상 B, 70점이상 C, 60점이상 D, 60점미만 F
#           (100~97점 A+,96~93점 A, 92~90점 A-, 89~87점 B+, 86~83점 B, 82~80점 B-)
score=int(input("시험점수를 입력하세요: "))
if score>=90:
    print("A",end="")
    if score>=97: print("+")
    elif score>=93: pass
    else: print("-")
elif score>=80:
    print("B",end="")
    if score>=87: print("+")
    elif score>=83: pass
    else: print("-")
elif score>=70:
    print("C")
elif score>=60:
    print("D")
else:
    print("F")


print("안녕",end="")  #줄단락 (,end="")
print("하세요")



