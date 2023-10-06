# Method Overriding in python

class Vehicles:
    """Base class for all vehicles"""

    def __init__ (self , name , manufacturer , color):
        print("Creating a vehicle")
        self.name = name
        self.manufacturer = manufacturer
        self.color = color

class Car(Vehicles):
    """Car class"""

    def __init__(self, name , manufacturer , color , year , wheels):
        print("Creating a car")
        super().__init__(name, manufacturer, color )
        self.year = year
        self.wheels = wheels

class MotorCycle(Vehicles):

    def __init__(self, name, manufacturer, color , year , cc):
        print("Creating a motorcycle")
        super().__init__(name, manufacturer, color)
        self.year = year
        self.cc = cc



c = Car("Nissan GTR" , "Nissan" , "Black" , 2022 , 4)
print(c.name , c.manufacturer , c.color ,c.year , c.wheels)