my_tuple = (1, 2, 3, 4)
print(my_tuple[0])   # 1

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