import random

list_min = []
list_plus = []

n = random.sample(range(-5, 5), 6)

for i in n:  
    if i > 0:
        list_plus.append(i)
    elif i < 0:
        list_min.append(i)
    else:
        print('Invalid number')

print(list_plus)
print(list_min)