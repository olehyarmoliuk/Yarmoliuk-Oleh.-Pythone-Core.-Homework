P = int(input('Enter a number '))
H = int(input('Enter a number '))

total_min = 0
total_aver = 0
total_max = 0

num_1 = 1 


while num_1 > 0: 
    num_1 = int(input('Enter a sequence of numbers '))
   
    if num_1 < P:
        total_min = total_min + num_1
    elif P < num_1 < H:
        total_aver = total_aver + num_1
    elif num_1 > H:
        total_max = total_max + num_1
    else:
        num_1 == P or num_1 == H
        break

print(total_min, total_aver, total_max)

        

       