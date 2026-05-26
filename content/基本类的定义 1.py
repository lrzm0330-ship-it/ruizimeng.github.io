class Car:
    color='white'   #属性名
    wheels=4        #属性名
    def move(self): #方法名 #self：代表当前对象自己，car1=Car（）：self就代表car1
        print('走着')
car1=Car()
car2=Car()
print(car1)
print(car2)

print(car1.color)
print(car2.color)
car1.move()
car2.move()
'''
面向对象编程思路：
对象 + 属性 + 行为，封装在一起
car.move()比move(car)更符合现实世界
'''
