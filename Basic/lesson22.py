"""                             List Attributes


In Python, a list is a data structure that stores a collection of items. It's defined by enclosing comma-separated values within square brackets `[ ]`. Lists are mutable, meaning their elements can be changed after the list is created.

"""

"""

1. Length (len): Returns the number of items in the list.

"""

my_list = [1, 2, 3, 4, 5]
length = len(my_list)
print(length)

"""

2. Indexing: Lists are indexed starting from 0. You can access elements using square brackets with the index.

"""

first_element = my_list[0]  # Accesses the first element
print(first_element)

"""

3. Slicing: Allows you to access a subset of elements in the list by specifying a start and end index.

"""

subset = my_list[1:4]  # Gets elements from index 1 to 3 (exclusive)
print(subset)

"""

4. Append: Adds an item to the end of the list.

"""

my_list.append(6)  # Adds 6 to the end of the list
print(my_list)

"""

5. Insert: Inserts an item at a specified position in the list.

"""

my_list.insert(2, 7)  # Inserts 7 at index 2
print(my_list)

"""

6. Remove: Removes the first occurrence of a specified item in the list.

"""

my_list.remove(3)  # Removes the first occurrence of 3
print(my_list)

"""

7. Pop: Removes and returns the item at the specified index. If no index is specified, it removes and returns the last item.

"""

popped_item = my_list.pop(2)  # Removes and returns item at index 2
print(popped_item)

"""

8. Clear: Removes all items from the list.

"""

my_list.clear()  # Clears all items from the list
print(my_list)

"""

9. Count: Returns the number of occurrences of a specified item in the list.

"""

count_of_2 = my_list.count(2)  # Returns the count of occurrences of 2
print(count_of_2)

"""

10. Index: Returns the index of the first occurrence of a specified item in the list.

"""

index_of_3 = my_list.index(3)  # Returns the index of first occurrence of 3
print(index_of_3)

"""

11. Sorting: Sorts the list in ascending order. 

"""

my_list.sort()  # Sorts the list in ascending order
print(my_list)

"""

12. Reverse: Reverses the order of items in the list.

"""
my_list.reverse()  # Reverses the order of items in the list
print(my_list)