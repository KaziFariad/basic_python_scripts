num = int(input())

bin = []

while(num > 0):
    if(num % 2 != 0):
        bin.append(1)
    else:
        bin.append(0)
    num //= 2

print("Number of 1's in the binary format of", num, "is:", bin.count(1))
