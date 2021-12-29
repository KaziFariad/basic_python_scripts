rows, columns = map(int, input().split())

print(rows, columns)
array = []
s = 0
if(rows == columns):
    for i in range(rows):
        array.append(list(map(int, input().split())))

print(array)
for i in range(rows):
    s += array[i][i]

print(s)
