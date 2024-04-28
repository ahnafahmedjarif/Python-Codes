"""         Function Arguments          


In Python, functions can accept arguments, which are values passed to the function when it is called. These arguments can be used within the function to perform computations or operation

"""

""" 1. 

    Positional Arguments: These are the most common type of arguments. They are passed to the     function in the order they are defined in the function's parameter list.
    
"""

def greet(name, greeting):
    return f"{greeting}, {name}!" # F-strings in  provide a concise and expressive way to format strings

print(greet("Jarif", "Hello"))  # Output: Hello, Jarif!

""" 2.

    Keyword Arguments: These are arguments preceded by a parameter name when you call a function.

"""

def greet(name, greeting):
    return f"{greeting}, {name}!"

print(greet(greeting="Hello", name="Python"))  # Output: Hello, Python!


""" 3.

    Default Arguments: You can provide default values for parameters, which are used when the caller doesn't specify a value for that parameter.

"""

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Python"))  # Output: Hello, Python!

""" 4.

    Variable-Length Positional Arguments (`*args`): These allow you to accept any number of positional arguments. The arguments are captured into a tuple.

"""

def add(*args):
    result = 0
    for num in args:
        result += num
    return result

print(add(1, 2, 3, 4))  # Output: 10