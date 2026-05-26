class Car:
    color='white'
    wheels=4
    def move(self):
        self.speed=0
        print('走着')
car1=Car()
car2=Car()
print(car1)
print(car2)

print(car1.color)
print(car2.color)
car1.move()

car2.height=2.0
print(car1,.speed)
print(car2.height)
#print(Car.speed)
