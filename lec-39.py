# Super method in python

class ParentClass:
    def parent_method(self):
        print("This is the parent method")

class ChildClass(ParentClass):
    def parent_method(self):
        print("Jarif")
        super().parent_method()
    def child_method(self):
        print("This is child method")
        super().parent_method()

child_obj = ChildClass()
child_obj.child_method()
child_obj.parent_method()

class Employee:
    def __init__(self , name , id ):
        self.name = name
        self.id = id
    
class Programmer(Employee):
    def __init__(self , name , id , lang):
         super().__init__(name , id)
         self.lang = lang

arham = Employee("Munahid Arham" , 4546)
jarif = Programmer("Jarif" , 4329 , "Python")

print(jarif.name, jarif.id , jarif.lang)