"""                         Tuple 

In Python, a tuple is an ordered collection of elements, similar to a list, but immutable. This means that once you create a tuple, you cannot change its contents. Tuples are defined using parentheses () and can contain elements of different types

"""

my_tuple = (1, 2, 3, 'a', 'b', 'c')

# we can access elements of a tuple using indexing, just like with lists
print(my_tuple[0])  # Output: 1
print(my_tuple[3])  # Output: 'a'

# Concatenating tuples
new_tuple = my_tuple + (4, 5, 6)
print(new_tuple)  # Output: (1, 2, 3, 'a', 'b', 'c', 4, 5, 6)

""" Tuple Attributes """

"""

1. count(value): This method returns the number of times a specified value appears in the tuple.

"""

print(my_tuple.count(2))  # Output: 2
print(my_tuple.count(3))  # Output: 3
print(my_tuple.count(4))  # Output: 0

"""

2. index(value): This method returns the index of the first occurrence of a specified value in the    tuple. If the value is not found, it raises a ValueError.

"""

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple.index(3))  # Output: 2
print(my_tuple.index(5))  # Output: 4