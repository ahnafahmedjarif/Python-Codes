"""                                input() function


`input()` is a built-in function in Python that allows you to prompt the user for input. It reads a line of text from the standard input (usually the keyboard), converts it to a string, and returns that string.


"""

name = input("Whats your name? ")
print("Welcome to python", name, "!") # output: Welcome to python `name` !

"""                                 int() function

`int()` is a built-in Python function used to convert a value to an integer (a whole number without any decimal). It can take various types of arguments and convert them into integers/

"""

number1 = int("10")
print(number1)  # Output: 10

number2 = int(True)
print(number2)  # Output: 1 (True = 1, False = 0)