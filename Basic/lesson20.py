"""     Enumerate Function


The `enumerate()` function in Python is a built-in function that allows you to loop over an iterable (such as a list, tuple, or string) while also keeping track of the index of the current item. It returns an enumerate object, which yields pairs of index and value for each item in the iterable.

"""

fruits = ['apple', 'banana', 'mango', 'cherry', 'lichi']

for index, fruit in enumerate(fruits):
    print(f"{index}. {fruit}")

"""
    Output:
    0. apple
    1. banana
    2. mango
    3. cherry
    4. lichi
"""

# We can also specify the `start` parameter to change the starting index:

marks = [70, 90, 30, 60, 97, 67]

for index, mark in enumerate(marks, start = 1):
    print(f"{index}. {mark}")

"""
    Output:
    1. 70
    2. 90
    3. 30
    4. 60
    5. 97
    6. 67
"""