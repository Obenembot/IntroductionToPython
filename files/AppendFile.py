selectedFile = open("file2.txt", 'a')
selectedFile.write("Appending this line here\n")
selectedFile.write("Appending this line Again\n")
selectedFile.close()

selectedFile = open("file1.txt", 'r')
content = selectedFile.read()
print(content)
selectedFile.close()
