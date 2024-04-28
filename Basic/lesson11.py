"""                         List in Python                 

List is a versatile and commonly used data structure that can hold an ordered collection of items. Lists are mutable, which means you can change their content after they are created
 
"""


"""   Creating a List:   """
# we can create a list by enclosing comma-separated values within square brackets []

my_list = [1, 2, 3, 4, 5]


""" Accessing Elements: """
# We can access individual elements of a list using indexing. Python uses zero-based indexing

print(my_list[0])  # Output: 1
print(my_list[2])  # Output: 3


"""    Slicing:    """
# We can extract a subset of a list using slicing

print(my_list[1:4])  # Output: [2, 3, 4]
print(my_list[2:3]) # Output: [3]


""" Modifying Elements: """
# We can modify elements in a list by accessing them and assigning new values

my_list[0] = 6
print(my_list)  # Output: [6, 2, 3, 4, 5]