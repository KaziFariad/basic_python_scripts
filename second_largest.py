non = int(input())
l = []
l = list(map(int, input().split()))
m = max(l)

while(l.count(m) != 0):
    l.remove(m)

print(max(l))
