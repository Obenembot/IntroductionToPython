def chageMe(value):
    print(f"Original value is {value}")
    value = 70
    print(f"new Value {value}")


def main():
    value = 90
    chageMe(value)
    print(f"Main value is {value}")


main()

print("========= Using Pass=========")
def passMe(name):
    pass
    print(name)

passMe("Pass me method")
