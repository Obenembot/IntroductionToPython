def greetings():
    print("Good Morning")


greetings()


def greetings(name):
    print("Greeting, ", name)


greetings('Oben-Embot')


def add_number(a: float, b: float):
    result = a + b
    print(f"Sum of {a} + {b} is", result)


add_number(12, 7)

add_number(b=12, a=7)

def greet(name, message = "How are you doing"):
    print(f"Hi {name}, {message}")

greet("Sam", )