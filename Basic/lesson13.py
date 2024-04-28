"""                     For Loop (Part - 2)                     """


# we can manually set incrementation and initialization in range function

for i in range(1, 20, 5): # initialization = 1, condition = i < 20, increment = i += 5
    print(i) 

# let's find a maximum number from a list using loop
    
numbers = [6, 1, 3, 9, 0, 10, 18, 6, 8]
max_n = numbers[0]    

for n in numbers:
    if n > max_n:
        max_n = n

print(max_n) # Output: 18

# Let's make a turtle program with loop

import turtle

turtle.speed(1)

for i in range(20):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(3)
    turtle.pendown()

turtle.exitonclick()