class Car:
    speed = 0
    tire = 4
    door = 5
    def speedUp(self,s):
        self.speed += s
        print("현재 속도 : ",self.speed)
        
class Sedan(Car):
    speed = 0
    tire = 4
    door = 5
    def speedUp(self,s):
        self.speed += s
        print("현재 속도 : ",self.speed)
    color = "red"        
    
c = Car()
# print(c.gireType)  # 없는 변수 출력시 에러

s = Sedan()
print(s.tire)  
    