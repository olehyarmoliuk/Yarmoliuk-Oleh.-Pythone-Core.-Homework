import random

rand_list = random.sample(range(0, 100), 5)

inp_list = []
count_1 = 0
while count_1 < 5:
    n = [int(input('Enter 5 numbers '))]
    count_1 += 1
    inp_list.extend(n)

sum_list = []
for i in range(0, len(rand_list)): 
    sum_list.append(rand_list[i] + inp_list[i]) 

print(rand_list)
print(inp_list)
print(sum_list)