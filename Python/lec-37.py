# Inctance variables vs class variables

class Employee:
    company_name =  "Apple"
    noOfEmployee = 0

    def __init__(self , name):
        self.name = name
        self.raise_amount = 0.02
        Employee.noOfEmployee += 1

    def show_details(self):
        print(f"The name of the employee is {self.name} and the raise amount in {self.noOfEmployee} sized {self.company_name} is {self.raise_amount}")

# Employee.show_details(emp1)
emp1 = Employee("Jarif")
emp1.raise_amount = 0.3
emp1.company_name = "Microsoft"
emp1.show_details()

Employee.company_name = "Google"

emp2 = Employee("Arham")
emp2.company_name = "Amazon"
emp2.show_details()
