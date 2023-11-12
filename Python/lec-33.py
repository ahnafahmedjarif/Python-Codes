# Constructor in python
# There are 2 types of constructor in python 
# 1. Defalut constructor  2. Parameterized constructor 

class Person:
    
    # This is Parameterized constructor
    def __init__(self , name , occ , age):
        print("Hey i am a person")
        self.name = name
        self.occ = occ
        self.age = age

    def info(self):
        print(f"{self.name} is a {self.occ} and {self.name} is {self.age} years old")
    
a = Person("Jarif" , "Developer" , 15)
b = Person("Adi" , "Cricketer" , 15)

# Calling the class
a.info()
b.info()