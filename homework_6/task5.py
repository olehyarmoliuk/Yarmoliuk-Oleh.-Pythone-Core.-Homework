lst = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

rows = len(lst)
columns = len(lst[0])

min_list = []

for i in range(0, columns):
    for j in range(0, rows):
        min_1 = lst[j][0]
        min_list.append(min_1)
        
print(max(min_list))