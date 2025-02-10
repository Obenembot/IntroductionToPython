with open("file2.txt", 'a') as file:
    file.write("First Line \n")
    file.write("Second Line \n")
    file.write("Last Line\n")
    file.write(str(90.70)+"-a\n")

'''
Read Lines without rstrip() or strip() or lstrip()
'''
with open("file2.txt", 'r') as file:
        file_line = file.read()
        print(file_line)

print("============ Without spacing =================")
with open("file2.txt", 'r') as file:
    sumOfWordCount = 0
    # for line in file:
    line  = file.readline().strip()
    while line != '':
        line = file.readline()
        # line = line.readline().rstrip("\n")
        print("Remove Space:", line.strip())
        sumOfWordCount += 1
    print(f"sumOfWordCount= {sumOfWordCount}")
    # find = file.readline().find("Second")
    # print(f"File word Second: {find}")
