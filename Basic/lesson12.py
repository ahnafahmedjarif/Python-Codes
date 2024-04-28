"""                             For Loop (Part - 1)                   

Loop: In programming, a "loop" is a control flow statement that allows code to be executed repeatedly based on a certain condition.

For Loop:  Used to iterate over a sequence (such as a list, tuple, string, or dictionary) or any iterable object for a fixed number of times.

"""

for i in range(10):
    print("Welcome to python!") 

for i in range(5):
    print(i)

""" let's make a square with turtle using for loop """

import turtle

turtle.speed(1)
turtle.shape("turtle")

for i in range(4):
    turtle.forward(100)
    turtle.left(90)

turtle.exitonclick()

""" lets make a program to add fifty 1's (1 X 50) """

result_1 = 0
for i in range(50):
    result_1 = result_1 + 1

print(result_1)

result_1 = 0
for _ in range(50): # we can use `_` instead of `i`
    result_1 += 1 # we can use if instead of `result_1 = result_1 + 1`


""" let's make an another program that adds numbers from 1 to 50 """

result_2 = 0
num = 1

for _ in range(50):
    result_2 += num
    num += 1

print(result_2)