# set a valiarable or age,
from tkinter.font import names

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
print("Hello,", _firstName)
