"""                             Nested Loop in Python                   

A nested loop is a loop inside another loop. This means that one loop will be executed within the body of another loop. Nested loops are often used when you need to perform repetitive tasks that involve multiple levels of iteration. 

"""

for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")


rows = int(input("Enter the number of rows: "))
collumns = int(input("Enter the number of collumns: "))
symble = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(collumns):
        print(symble, end = " ")
    print()


import turtle 

turtle.shape("turtle")
turtle.speed(1)

for side_length in range(50, 100, 10):
    for i in range(4):
        turtle.forward(side_length)
        turtle.left(90)

turtle.exitonclick()

"""                         Loop in list                        """

saarc = ["Bangladesh", "Afghanistan", "Bhutan", "Nepal", "India", "Pakistan", "Sri Lanka"]

for country in saarc:
    print(country)