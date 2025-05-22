selectedFile = open("file1.txt", 'a')
# selectedFile.write("How are you doing\nAnother Great day")
# selectedFile.close()
selectedFile1 = open("file1.txt", 'd')
content = selectedFile1.read()
print(content)

selectedFile.write("\n"+content)
# selectedFile.close()