

for i in [2,3,4,5,6,7,8]:
    print(i, end=" | ")
ab = "How are you".split()
print(ab)
a = 90

print("How are you " , a)
for b in range(5):
    print(b, end=", ")

print()
TAX_PERCENT: float = 0.15

value = "Feels {} to be {}"

value: str = value.format("Good", "Good")

print(value)
name = "Sam"
value = f'{name} is my name'
print(value)

balance = 52.983235343

print("Bank Balance is %.2f" % balance)
print("Bank Balance is %s %d" % (balance ,balance))

print(TAX_PERCENT)

'''
Even after specifying the type for a variable, the value can still be changed. 
But there will be a warning though it still works. 
'''
value = 10
print(value)