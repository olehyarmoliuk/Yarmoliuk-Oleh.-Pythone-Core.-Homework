mtrx = [[1, 2, 3,], 
        [4, 5, 6], 
        [7, 8, 9]]
    
rows = len(mtrx)
columns = len(mtrx[0])

sum_rows = [sum(i) for i in mtrx]
print(sum_rows)


sum_columns = [sum(row[i] for row in mtrx) for i in range(columns)]
print(sum_columns)

mtrx[0].append(sum_rows[0])
mtrx[1].append(sum_rows[1])
mtrx[2].append(sum_rows[2])
mtrx.append(sum_columns)
mtrx[3].append(sum_rows[0] + sum_rows[1] + sum_rows[2])

print(mtrx)