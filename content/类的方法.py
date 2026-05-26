class Car:
    wheels=4
    def move(self):
        print(self,'走着')
    @classmethod
    def stop(cls):
        print(cls,'立定')
car1=Car()
car2=Car()
print(car1)
print(car2)
car1.move()
car2.move()
#Car.move()

car1.stop()
Car.stop()
