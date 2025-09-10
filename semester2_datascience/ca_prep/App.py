import random as rd


def set_numbers(value1, value2):
    print("Init")
    print("Value1:", value1, end=", ")
    print("Value2:", value2)


def generate_numbers():
    return rd.randrange(1, 100)


set_numbers(12, 34)

list = generate_numbers()

print("List:", list)