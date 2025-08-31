my_tuple = (1, 2, 3, 4)
print(my_tuple[0])  # 1

# Tuples cannot be changed:
# my_tuple[1] = 10  ❌  --> Error

# Packing & Unpacking Tuples
person = ("Sam", 25, "Developer")
name, age, job = person
print(name)  # Sam
print(person)  # Sam

count = person.count(25)

print(count)
ages = (25, 30, 35, 40, 25, 30, 25)
#  Can not do lots of operations like list
print(ages)

'''
In Python, a tuple is an ordered, immutable (unchangeable) collection used to store multiple items in a single variable. Tuples are one of Python’s built-in data structures, along with lists, sets, and dictionaries.

They are defined by placing elements inside parentheses () and separating them with commas.

Key Characteristics of Tuples
Feature	Description	Example
Ordered	Items have a fixed order and can be accessed using an index.
	t = (10, 20, 30) → t[0] → 10
Immutable	Once created, elements cannot be changed, added, or removed.
	t[1] = 40 ❌ (will raise an error)
Heterogeneous	Can store different data types in the same tuple.
	t = (1, "Sam", 3.14, True)
Allow Duplicates	Tuples can have duplicate values.
	t = (1, 1, 2)
Indexed Access	Access items using positive or negative indexes.
	t[-1] → Last element
'''
