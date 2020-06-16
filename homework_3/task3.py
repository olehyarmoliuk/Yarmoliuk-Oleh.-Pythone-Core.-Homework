num_1 = int(input('Enter a number from -999999 to 999999 '))

if num_1 == 0:
    print("zero one-digit")    
elif 0 < num_1 < 10:
    print("positive one-digit")
elif 10 < num_1 < 100:
    print("positive two-digit")
elif 100 < num_1 < 1000:
    print("positive three-digit")
elif 1000 < num_1 < 10000:
    print("positive four-digit")
elif 10000 < num_1 < 100000:
    print("positive five-digit")
elif 100000 < num_1 < 1000000:
    print("positive six-digit")
elif 0 > num_1 > -10:
    print("negative one-digit")
elif -10 > num_1 > -100:
    print("negative two-digit")
elif -100 > num_1 > -1000:
    print("negative three-digit")
elif -1000 > num_1 > -10000:
    print("negative four-digit")
elif -10000 > num_1 > -100000:
    print("negative five-digit")
elif -100000 > num_1 > -1000000:
    print("negative six-digit")
else:
    print('Incorrect value')