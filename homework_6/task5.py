lst = [[4, 2, 6],
       [1, 9, 8],
       [7, 5, 3]]

rows = len(lst)
columns = len(lst[0])

min_1 = []

for i in range(columns):
    max_1 = lst[i][1]
    for j in range(rows):
        if lst[j][i] < max_1:
            max_1 = lst[j][i]
            min_1.append(max_1)
        
        
print(min_1)
print([max(min_1)])