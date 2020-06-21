import math

r = float(input('Enter radius length '))
s = math.pi * r ** 2 
print("Stage area is", s, 'm2')
h = float(input("Enter length of hall side ")) ** 2
print('Hall area is', h, 'm2')
k = float(input('Enter possible distance to the wall '))


if math.sqrt(s) >= 2 * (k + r):
    print("It is impossible")
else:
    print("It is possible")