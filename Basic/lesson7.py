"""                                        Conditional Logic            

the `if` statement is used for conditional execution. It allows you to execute a block of code only if a certain condition is true. You can also include an `else` statement to provide an alternative block of code to execute if the condition is false. Here's the basic syntax:

    if condition:
        # code to execute if the condition is true
    else:
        # code to execute if the condition is false

"""

x = 10

if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")


""" we can also use elif (short for "else if") to check for multiple conditions. Here's an example: """

y = 10

if y > 5:
    print("y is greater than 5")
elif y == 5:
    print("y is equal to 5")
else:
    print("y is less than 5")