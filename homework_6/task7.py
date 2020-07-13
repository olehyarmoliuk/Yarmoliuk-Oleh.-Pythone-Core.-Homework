mtrx = [[8, 213, 6], 
        [1, 9, 11], 
        [85, 123, 22]]

rows = len(mtrx)
columns = len(mtrx[0])

mtrx_rev = [[0] * rows for i in range(columns)]

for i in range(rows):
    for j in range(columns):
        mtrx_rev[j][i] = mtrx[i][j]

mtrx_rev[0].sort()
print(mtrx_rev)