# set a valiarable or age,
from tkinter.font import names
from unicodedata import decimal

age = 90
"""
Here we can add a separator between the 2 argument.
Note:  
"""
print("Hello, IntelliJ with Python!, ", age, sep=" R")

# print always goes to next line but can be made to single line by adding the end variable
print("Hello, IntelliJ with Python!, ", age, end=" ")
print("Hello, IntelliJ with Python!, ", age)

age = "How are you doing"
print("change from 'number' value to 'string' ", age, sep=" = ")

print(type(age))
# Input is use to collect data from a user.
_firstName = input("Enter First Name:")

_age = input("Enter Age: ")

print("================== Data Collected ===========================")
print("Hi am ", _firstName, end="")
print(" And I'm " + _age + " years old")

'''
All input are in string format
to convert to data type use
int(_age), float(_age), decimal(_age)
Decimal fails complains of argument 1 must be a unicode character, not str
'''
#
_age = float(_age)

print(type(_age))
