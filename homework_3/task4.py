from math import pi

r = float(input('Enter radius length '))
stage_1 = pi * r ** 2 
print("Stage area is", stage_1, 'm2')
hall_1 = float(input("Enter length of hall side ")) ** 2
print('Hall area is', hall_1, 'm2')
k = float(input('Enter possible distance to the wall '))
freeSpace = hall_1 - k * 4
print("Possible place for the stage is", freeSpace, 'm2')


if stage_1 > freeSpace:
    print("It is impossible")
else:
    stage_1 < freeSpace
    print("It is possible")