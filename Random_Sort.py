import random
l = list(map(int, input().split(" ")))
count = 0
while(l != sorted(l)):
    i = random.randrange(len(l))
    j = random.randrange(len(l))
    count += 1
    tem = l[i]
    l[i] = l[j]
    l[j] = tem
print("Total number of iterations taken are:", count)
print(l)
