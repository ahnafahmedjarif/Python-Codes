"""             Set

In Python, a set is an unordered collection of unique elements. Unlike lists or tuples, sets do not allow duplicate elements. Sets are defined using curly braces `{}` or by using the `set()` constructor.

"""

my_set = {1, 2, 3, 4, 5}

# Or using the set() constructor:
my_set = set([1, 2, 3, 4, 5])

"""                 Set Attributes              """

"""

1. add(element): Adds a single element to the set. If the element is already present, the set remains unchanged.

"""

my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

"""

2. remove(element): Removes the specified element from the set. Raises a KeyError if the element is not present in the set.

"""

my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)  # Output: {1, 3}


"""

3. discard(element): Removes the specified element from the set if it is present. If the element is not present, it does nothing.

"""

my_set = {1, 2, 3}
my_set.discard(2)
print(my_set)  # Output: {1, 3}


"""

4. pop(): Removes and returns an arbitrary element from the set. If the set is empty, it raises a KeyError.

"""

my_set = {1, 2, 3}
element = my_set.pop()
print(element)  # Output: An arbitrary element, e.g., 1
print(my_set)   # Output: {2, 3}


"""

5. clear(): Removes all elements from the set.

"""

my_set = {1, 2, 3}
my_set.clear()
print(my_set)  # Output: set()
