"""
1. What is a Set?
A set in Python is an unordered, mutable collection of unique elements.
Sets are similar to mathematical sets.
Key Features
Unordered → No guaranteed order of elements.
Unique Items → Duplicates are automatically removed.
Mutable → Can add and remove items.
Unindexed → Elements are not accessed by position.
Supports set operations → union, intersection, difference, etc.


Method	Description	Example
remove(x)	Removes element x but throws an error if not found	s.remove(3)
discard(x)	Removes element x without error	                    s.discard(3)
pop()	    Removes and returns a random item               	s.pop()
clear()	    Removes all elements	                            s.clear()
"""

fruits = {"apple", "banana", "cherry", "banana", "apple"}

print(fruits)
print(type(fruits))
fruits.add("orange")
fruits.update({"green"})

for f in fruits:
    print(f, end=", ")

a = {1, 2, 3, 4, 5}
b = set([4, 5, 6, 7, 8])

# Union
union = a | b
print("\nUnion:", union)
union = a.union(b)
print("\nUnion:", union)
intersection = (a & b)
print("Intersection: ", intersection)
print("Intersection: ", a.intersection(b))

difference = a - b
print("difference: ", difference)
print("difference: ", a.difference(b))

symmetric_difference = a ^ b
print("symmetric_difference: ", symmetric_difference)
print(symmetric_difference)

print('issubset: ', a.issubset(b))
print('isdisjoint: ', a.isdisjoint(b))
print('issuperset: ', a.issuperset(b))

fs = frozenset([1, 2, 3, 4])

# fs. add(5)  # AttributeError: 'frozenset' object has no attribute 'add'
print("FS: ",fs)