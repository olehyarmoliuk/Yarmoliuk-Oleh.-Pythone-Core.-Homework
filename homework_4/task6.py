pos_num, neg_num = 0, 0

while True:
<<<<<<< HEAD
=======
    
>>>>>>> 7fcc4039af56a13b5e8d3ff28969a40c49499912
    num_1 = int(input('Enter your number. To stop inputting "press 0" '))
 
    if num_1 > 0:
        pos_num += 1
    elif num_1 < 0:
        neg_num += 1
<<<<<<< HEAD
    else:
=======
    else: 
>>>>>>> 7fcc4039af56a13b5e8d3ff28969a40c49499912
        if num_1 == 0:
            per = 100/(pos_num + neg_num)
            print("Percentage of positive numbers: ", int(pos_num * per))
            print("Percentage of negative numbers: ", int(neg_num * per))
<<<<<<< HEAD
            break
=======
            break
>>>>>>> 7fcc4039af56a13b5e8d3ff28969a40c49499912
