matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

rows = 4
cols = 3

rowsums = []
colsums = []
rowtemp = 0
coltemp = 0

for i in range(0, rows*cols, cols):
    rowtemp = 0
    for j in range(cols):
        rowtemp += matrix[i+j]
    rowsums.append(rowtemp)

for i in range(cols):
    coltemp = 0
    coltemp += sum([matrix[i + j*cols] for j in range(rows)])
    colsums.append(coltemp)

print(rowsums, colsums)
print(max(rowsums) + max(colsums))
