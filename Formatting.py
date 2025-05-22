
TAX_PERCENT: float = 0.15

value = "Feels {} to be {}"

value: str = value.format("Good", "Good")

print(value)
name = "Sam"
value = f'{name} is my name'
print(value)

balance = 52.983235343

print("Bank Balance is %.2f" % balance)

print(TAX_PERCENT)

'''
Even after specifying the type for a variable, the value can still be changed. 
But there will be a warning though it still works. 
'''
value = 10
print(value)