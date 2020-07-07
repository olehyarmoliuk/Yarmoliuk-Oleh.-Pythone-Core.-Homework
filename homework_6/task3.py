list_1 = [22, 13, 10, 11, 15, 17, 2, 19, 18, 5, 16]
list_2 = []

for i in list_1:
    if i % 2 == 0:
        list_2.append(list_1.index(i))
print(list_2)