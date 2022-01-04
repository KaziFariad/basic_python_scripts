def Print(n, ms):
    for i in range(n):
        for j in range(n):
            print(ms[i][j], end=" ")
        print()


def Magic_Square(n):
    ms = []
    for i in range(n):
        l = []
        for j in range(n):
            l.append(0)
        ms.append(l)
    size = n*n
    count = 1
    sum = n*(n**2+1)/2
    p = n//2
    q = n-1
    while(count <= size):
        if(p == -1 and q == n):
            p = 0
            q = n-2
        else:
            if(q == n):
                q = 0
            if(p < 0):
                p = n-1
        if(ms[p][q] != 0):
            p = p+1
            q = q-2
            continue
        else:
            ms[p][q] = count
            count += 1
        p = p-1
        q = q+1
    Print(n, ms)


number = int(input("Enter a number: "))
Magic_Square(number)
