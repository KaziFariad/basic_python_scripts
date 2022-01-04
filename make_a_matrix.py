x, y = map(int, input().split(" "))
c = 1
m = []
for i in range(x):
    l = []
    for j in range(y):
        l.append(c)
        c += 1
    m.append(l)
for i in range(x):
    for j in range(y):
        if(j == y-1):
            print(m[i][j], end="")
        else:
            print(m[i][j], end=" ")
    if(i == x-1):
        print(end="")
    else:
        print()
