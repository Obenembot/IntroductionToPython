"""
1. What is a Dictionary?

A dictionary in Python is an unordered, mutable collection of key-value pairs.

Each item has a key and a value.

Keys are unique and immutable (strings, numbers, tuples).

Values can be any data type and duplicated.

Introduced as { key: value }.


student = {
    "name": "John",
    "age": 21,
    "course": "Python"
}
print(student)      # {'name': 'John', 'age': 21, 'course': 'Python'}
print(type(student))  # <class 'dict'>


person = {"name": "Alice", "age": 25}
person = dict(name="Alice", age=25)
student = {"name": "John", "age": 21}
print(student["name"])
print(student.get("age"))      # 21
student["grade"] = "A"
student.update({"age": 23, "course": "Python"})

Method	Description	Example
dict.keys()	Returns all keys	student.keys()
dict.values()	Returns all values	student.values()
dict.items()	Returns list of (key, value) pairs	student.items()
dict.get(key)	Gets value safely	student.get("age")
dict.update()	Updates dictionary	student.update({...})
dict.pop(key)	Removes key & returns value	student.pop("name")
dict.clear()	Empties dictionary	student.clear()

student = {"name": "John", "age": 21, "grade": "A"}
for key in student:
    print(key)
"""

student  = {"name": "John", "age": 21, "grade": "A"}

print("student:", student)
print("type(student):", type(student))
print("student['name']:", student["name"])
print("student.get('name'):", student.get("name"))
student.pop("name")
print("student pop name:", student)
student.update({"age": 23, "course": "Python"})
student["remark"] = "Passed"
print("after update student:", student)


person = dict(name="Alice", age=25)
print("person:", person)
print("===  key, student[key] ===")
for key in student:
    print(key, ":", student[key])

print("===  key, value in student.items() ===")
for key, value in student.items():
    print(key, "->", value)
print("=== Using items() ===")
for item in student.items():
    print(item)
print("=== Using values() ===")
for value in student.values():
    print(value)
print("=== Using keys() ===")
for key in student.keys():
    print(key)


del  student["remark"]

print(student)