l = list(map(int, input().split(",")))
# 1,2,3,4,5
e = []
for i in range(len(l)):
    sum = 0
    for j in range(len(l)):
        if(i != j):
            print(i, j)
            sum = sum+l[j]
    e.append(sum)

for i in range(len(e)):
    if(i != len(e)-1):
        print(str(e[i])+",", end="")
    else:
        print(e[i])

print(e)
