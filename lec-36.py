# Inheritance in python

class Employee:
    def __init__(self , name , id):
        self.name = name
        self.id = id
    def showDetails(self):
        print(f"The name of employee {self.id} , is {self.name}")

class Programmer(Employee):
    def showLanguages(self):
        print("The defalut language is python")

e1 = Employee("Siyam", 5465)
e1.showDetails()

e2 = Programmer("Jarif" , 1231)
e2.showDetails()
e2.showLanguages()

