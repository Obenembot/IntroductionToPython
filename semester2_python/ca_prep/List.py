_list = [10, 30, 20, 40, 50, 60]
print(_list)

print(_list[0])  # Accessing the first element

_list[5] = 70

print(_list)

print(_list[1:4])  # Slicing the list from index 1 to 3

print("==========")
print(_list)
_list.append(80)
_list.sort()
_list.sort(reverse=True)
print(_list)

# Creating an empty list
empty_list = list()
empty_list = list((1, 2, 3, 4, 9, 5, 6, 7, 8, 9, 10))

del empty_list[0]

print(empty_list)

new_List = empty_list[1:5:1]
print(new_List)
print(empty_list)

print("Max: ", max(empty_list))
print("MIn: ", min(empty_list))
print("Sum: ", sum(empty_list))
print("Length: ", len(empty_list))
print("Count: ", empty_list.count(9))

print("Last Index: ", empty_list[-2])  # To access from the last index backwards at that position

print("==========FRUITS==========")
fruits = ["apple", "banana"]

fruits.append("cherry")
fruits.insert(0, "orange")  # Inserts at the specified index
fruits.extend(["mango"])  # Extends each character of the string as a separate element
print("Fruits: ",fruits)

for fruit in fruits:
    print(fruit)


print('apple' in fruits)  # Check if 'apple' is in the list)
"""
A list in Python is a collection data type used to store multiple items in a single variable.
Lists are:

Ordered → The items maintain the order in which they were added.

Mutable → You can add, update, or remove elements.

Heterogeneous → Can store different data types in one list.

Indexed → Items are accessed by their index (starting from 0).

Dynamic → Lists can grow or shrink in size.

"""
