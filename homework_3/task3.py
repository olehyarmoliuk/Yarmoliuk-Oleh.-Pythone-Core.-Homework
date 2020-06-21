num_1 = int(input('Enter a number from -999999 to 999999 '))

if num_1 < 0:
    print('negative')
else:
    print('positive')

if num_1 == 0:
    print("zero one-digit")  

if 0 < abs(num_1) <= 9:
    print("one-digit")
elif 9 < abs(num_1) <= 99:
    print("two-digit")
elif 99 < abs(num_1) <= 999:
    print("three-digit")
elif 999 < abs(num_1) <= 9999:
    print("four-digit")
elif 9999 < abs(num_1) <= 99999:
    print("five-digit")
elif 99999 < abs(num_1) <= 999999:
    print("six-digit")
else:
    print('Incorrect value')    