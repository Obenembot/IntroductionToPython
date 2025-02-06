x = 31

# Using Single Alternative decision Diamond
if x > 10:
    print(f"X {x} is greater than 10")

# Dual Alternative Decision structure.
if x == 10:
    print(f"X {x} is equal to 10")
else:
    print(f"X {x} is not equal to 10")

if x == 10:
    print(f"X {x} is equal to 10")
# elif 10 < x < 15:
elif x > 10 and x < 15:
    print(f"X {x} > 10 & {x} < 15")
else:
    print("No condition is met")



string_1 = 'Hello'
string_2 = 'hello'
if string_1 == string_2:
    print(f"{string_2} and {string_1} are the same")

if string_1 != string_2:
    print(f"{string_2} and {string_1} are not the same")
print(f"End of file")

string_2 = "World"
if string_1 > string_2:
    print(f"{string_1} is greater than {string_2}")
else:
    print(f"{string_1} is not greater than {string_2}")
    if string_1.__contains__("H"):
        print("string_1 contains H")