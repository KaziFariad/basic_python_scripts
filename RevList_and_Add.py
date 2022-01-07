n = input("Enter the number of numbers:")
x = [int(i) for i in input("Enter the elements:").split(" ")]
y = []
for i in range(len(x)-1, -1, -1):
    y.append(x[i])

print(y)
for i in range(len(x)):
    print(x[i]+y[i])
