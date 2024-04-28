"""                         While Loop          

`while` loop is used to repeatedly execute a block of code as long as a specified condition is true

"""

i = 0
while i < 5:
    print(i)
    i += 1

""" Let's print a multiplication table with while loop """

n = int(input("Plase enter a number: "))

m = 1
while m <= 10:
    print(n, "x", m, "=", n*m)
    m += 1


""" Let's make a design with turtle """

import turtle 

turtle.color("black")
turtle.speed(5)

counter = 0
while counter < 36:
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.right(10)
    counter += 1

turtle.exitonclick()