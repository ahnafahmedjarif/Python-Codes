"""     Creating a new class       """

# If I want to make a car racing game, I need make a car objects
# Now, there are many data attributes (characteristics) or method (functions).

# Attributes:
    # 1. Name
    # 2. Manufacturer
    # 3. color
    # 4. year
    # 5. cc

# Methods:
    # 1. Start
    # 2. Brake
    # 3. Drive
    # 4. Turn
    # 5. Change gear

"""Structure of a class"""
"""
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-n>

"""

class Car: # "Car" is the name of the class

    # ! Data attributes setion
    # Here the name, color etc.. are the data attributes

    #__init__ is a special method (also called a constructor) that is automatically called when an object of a class is created. It initializes the attributes of the class and allows you to pass initial values for the object.
    def __init__(self, name, color, manufacturer, year, cc):
        self.name = name
        self.color = color
        self.manufacturer = manufacturer
        self.year = year
        self.cc = cc

    # ! Method section

    def start(self):
        print(f"{self.name} is starting")
    
    def brake(self):
        print(f"{self.name} is stopping")

    def turn(self, direction):
        print(f"{self.name} is turning {direction}")

    def change_gear(self):
        print(f"{self.name} is changing gear")

    
# Creating object

car1 = Car("Supra", "red", "Toyota", 2019, 2000)    
car2 = Car("Gran Coupe", "White", "BMW", 2020, 2500)

print(car1.name)
print(car1.color)
print(car1.manufacturer)

car1.start()
car1.turn("Right")
car1.brake()

print(car2.name)
print(car2.year)
print(car2.cc)

car2.start()
car2.change_gear()
car2.turn("Left")