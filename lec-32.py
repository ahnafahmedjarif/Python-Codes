# Object Oriented Programming

# class
class Person:
    name = "Jarif"
    occupation = "Student"
    net_worth = 0 
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
b = Person()
c = Person()

a.name = "Arham"
a.occupation = "Sweeper"

b.name = "Siyam"
b.occupation = "Doctor"
# print(a.name , a.occupation)

a.info()
b.info()
c.info()