a = 5
while a >= 1:
    print(a, sep="aaaa", end=" ")
    a = a - 1

print("============ End of While Loop=============")

b = 0;
for b in [0, 1, 2, 3, 4, 15, 6, 7]:
    print("array[0...10] = ", b, )

c = 0
for v in range(5):
    print(" value of ", v, end=" |||| ")

print("=========== Range with 3 arguments ===================")
for b in range(1, 10, 2):
    print(b, end=" ")

print("=========== Range with 3 arguments ===================")

for b in range(1, 9):
    square = b **2
    print(f"The square of {b} is {square}")
   # print(b, end=" ")
