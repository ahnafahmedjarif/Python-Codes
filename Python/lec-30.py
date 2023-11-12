# Map filter and reduce in python

# MAP
def cube(x):
    return x*x*x
print(cube(2))

l = [1, 2, 3, 4 , 5, 6]
# newl = []
# for item in l:
#     newl.append(cube(item))

newl = list(map(cube , l)) # Using map method
print(newl)

# FILTER

def filter_function(a):
    return a>4

newnewl = filter(filter_function, l)
print(newnewl)

from functools import reduce

# List of Numbers
numbers = [1, 3,5,6,7,8]

# calcurate the sum of the numbers using the reduce function
def sum(x , y):
    return x + y

mysum = reduce(sum , numbers)
print(mysum)