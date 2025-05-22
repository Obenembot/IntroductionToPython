name: str = "Sampson"

message: str = "Hello, " + name
print(message)

message: str = f"Hello, {name}"
print(message)

message: str = "Hello, {}".format(name)
print(message)

message:str = "Hello, %s" % name
print(message)

words = ["Python", "is", "awesome"]
message = " ".join(words)
print(message)

message = ""
for a in words:
    message += " " + a
print(message.strip())

for a in range (1,7,4):
    print(a)

print("=========================")
a = 5
while a < 10:
    print(a)
    a += 1