class Car:
    color='white'
    wheels=4
    def move(self):
        print('走着')
car1=Car()
car2=Car()
print(car1)
print(car2)

print(car1.color)
print(car2.color)
car1.move()
car2.move()

print(car1.wheels)
print(Car.wheels)
#car1.wheels=1
print(Car.wheels)

car.move()
Car.move()
