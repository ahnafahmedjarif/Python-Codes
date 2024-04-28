"""                         Dictionary

In Python, a dictionary is a mutable, unordered collection of key-value pairs. Dictionaries are defined using curly braces `{}`, and each key-value pair is separated by a colon `:`.Dictionaries are commonly used for storing and retrieving data based on keys, providing fast lookup times.

"""

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

"""         Dictionary Attributes       """

"""

1. keys(): Returns a view object that displays a list of all the keys in the dictionary.

"""

print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'city'])

"""

2. values(): Returns a view object that displays a list of all the values in the dictionary.

"""

print(my_dict.values())  # Output: dict_values(['John', 30, 'New York'])

"""

3. items(): Returns a view object that displays a list of tuples, where each tuple is a key-value pair.

"""

print(my_dict.items())  # Output: dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])

"""

4. get(key[, default]): Returns the value associated with the specified key. If the key is not found, it returns the default value (which defaults to None if not provided).

"""

print(my_dict.get('name'))  # Output: 'John'
print(my_dict.get('gender', 'Unknown'))  # Output: 'Unknown'

"""

5. pop(key[, default]): Removes the key and returns its associated value. If the key is not found, it raises a KeyError, unless a default value is provided.

"""

age = my_dict.pop('age')
print(age)  # Output: 30
print(my_dict)  # Output: {'name': 'John', 'city': 'New York'}

"""

6. clear(): Removes all items from the dictionary.

"""

my_dict.clear()
print(my_dict)  # Output: {}
