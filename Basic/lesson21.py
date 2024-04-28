""" String Attributes

string objects are immutable sequences of characters. This means once a string is created, it cannot be changed. However, there are several string attributes and methods available for working with strings. 

"""

""" 

1. `str.lower()`: Returns a copy of the string with all uppercase characters converted to lowercase. 

"""

s = "Hello, World!"
print(s.lower())  # Output: hello, world!

"""

2. `str.upper()`: Returns a copy of the string with all lowercase characters converted to uppercase.

"""

s = "Hello, World!"
print(s.upper())  # Output: HELLO, WORLD!

"""

3. `str.strip()`: Returns a copy of the string with leading and trailing whitespace removed.

"""

s = "   Hello, World!   "
print(s.strip())  # Output: Hello, World!

"""

4. `str.isdigit()`: Returns `True` if all characters in the string are digits, otherwise `False`.

"""

s = "12345"
print(s.isdigit())  # Output: True

"""

5. str.isalpha(): Returns `True` if all characters in the string are alphabetic (letters), otherwise `False`.

"""

s = "Hello"
print(s.isalpha())  # Output: True

"""

6. `str.startswith(prefix)`: Returns `True` if the string starts with the specified prefix, otherwise `False.`

"""

s = "Hello, World!"
print(s.startswith("Hello"))  # Output: True

"""

7. `str.endswith(suffix)`: Returns `True` if the string ends with the specified suffix, otherwise `False`.

"""

s = "Hello, World!"
print(s.endswith("World!"))  # Output: True

"""

8. `str.find(sub, start=0, end=-1)`: Returns the lowest index in the string where substring `sub` is found. Returns `-1` if `sub` is not found. You can also specify optional `start` and `end` parameters to search within a specific range of the string.

"""

s = "Hello, World!"
print(s.find("World"))  # Output: 7

"""

9. `str.replace(old, new, count=-1)`: Returns a copy of the string with all occurrences of substring `old` replaced by `new`. If `count` is specified, only the first `count` occurrences are replaced. 

"""

s = "Hello, World!"
print(s.replace("Hello", "Hi"))  # Output: Hi, World!
