# List = [] mutable, ordered
#  tuple () immutable, ordered
# Distinction => Key value pair {name: '',age: 0}
# Sets => Sets store unique, unordered items.
# List example
fruits = ["apple", "banana", "mango"]
fruits.append("orange")
print("List: ",fruits)  # ['apple', 'banana', 'mango', 'orange']

# Tuple example
colors = ("red", "blue", "green")

print("Tuple: ",colors)  # blue

#  Dictionary and Set => storing unique and structured data


def print_person ():

    person = {
        "name": "Sampson",
        "age": 25,
        "city": "Pretoria"
    }

    for key, value in person.items():
        print(key, value)
    print("========= Print Just the values ======")
    for value in person.values():
            print(value)
def set_manipulation():
    ages = {1,2,3,4,3,43,34,3,2,32,4,5} # Set
    print(ages)

def set_manipulation(age):
    ages = {1,2,3,4,3,43,34,3,2,32,4,5} # Set
    print(ages)

print_person()
set_manipulation()


