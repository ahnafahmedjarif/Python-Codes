"""                                       Data Types in Python

In Python, like in many programming languages, data types define the type of data that can be stored and manipulated. Here are some commonly used data types in Python:

1. Numeric Types:

    int: Integers, e.g., 5, -3, 1000.
    float: Floating-point numbers, e.g., 3.14, -0.001, 2.0.

2. Boolean Type:

    bool: Boolean values, which can be either True or False.

3. Sequence Types:

    str: Strings, e.g., 'hello', "world", 'Python'.
    list: Ordered collections of items, e.g., [1, 2, 3], ['apple', 'banana', 'orange'].
    tuple: Immutable ordered collections of items, e.g., (1, 2, 3), ('a', 'b', 'c')

4. Mapping Type:

    dict: Unordered collections of key-value pairs, e.g., {'name': 'John', 'age': 30}.

5. Set Types:

    set: Unordered collections of unique items, e.g., {1, 2, 3}, {'apple', 'banana', 'orange'}.
    frozenset: Immutable version of a set.

         *** we can check the type of a variable or a value using the type() function. ***
"""

x = "python"
print(type(x)) # output: <class 'str'>

y = 5
print(type(y)) # output: <class 'int'>

z = 6.89
print(type(z)) # output: <class 'float'>