pos_num, neg_num = 0, 0

while True:
    num_1 = int(input('Enter your number '))
 
    if num_1 > 0:
        pos_num += 1
    elif num_1 < 0:
        neg_num += 1
    else:
        per = 100/(pos_num + neg_num)
        print("Percentage of positive numbers: ", int(pos_num * per))
        print("Percentage of negative numbers: ", int(neg_num * per))
        break