x = 10
y = 16

a = 5
b = 5

result = a == b and x > y
print("a == b and x > y ", result)

result = a == b or x > y
print("a == b or x > y ", result)


result = not(a == b or x > y)
print("not(a == b or x > y) ", result)