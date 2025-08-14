def calculate(value1: int = 10, value2=2):
    result = int(value1) + int(value2)
    print(result)
    return result


value1 = input("Enter Int Value")
result1 = calculate(value1, 5)

print(result1)

with open("../FirstPythonProject.iml", 'r') as file:
    # readlines = file.readlines() # Reads with the format in the file
    # print(readlines)
    print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
    # read = file.read()  # Reads in the same format
    # print("Read Method: ", read)
    readLine = file.readline()  # Reads the first line in the same format
    while readLine != "":
        print("readLine Method: ", readLine)
        readLine = file.readline()
