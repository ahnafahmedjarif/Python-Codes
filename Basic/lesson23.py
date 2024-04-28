"""                         List Comprehensions

List comprehensions in Python provide a concise way to create lists. 

syntax:

new_list = [expression for item in iterable if condition]

"""

# Doubling each element in a list:
original_list = [1, 2, 3, 4, 5]
doubled_list = [x * 2 for x in original_list]
# doubled_list will be [2, 4, 6, 8, 10]

# Filtering even numbers from a list:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]
# even_numbers will be [2, 4, 6, 8, 10]

# Creating a list of squares of numbers:
squares = [x**2 for x in range(1, 6)]
# squares will be [1, 4, 9, 16, 25]

# Creating a list of tuples from two lists:
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
combined_list = [(x, y) for x in list1 for y in list2]
# combined_list will be [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3)]