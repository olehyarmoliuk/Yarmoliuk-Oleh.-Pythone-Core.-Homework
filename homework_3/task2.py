from math import pi
q = input('Choose a rectangle, a triangle, or a circle: ')
       
if q == 'rectangle':
    length_1 = int(input('What is the length? '))
    width_1 = int(input('What is the width? '))
    print("Square of the rectangle is", length_1 * width_1)
elif q == 'triangle':
    h = int(input('What is the leg length? '))
    b = int(input('What is the base length? '))
    print ("Square of the triangle is", 0.5 * h * b)
elif q == 'circle':
    r = int(input('What is the radius length? '))
    print('Square of the circle is', pi * r ** 2)
else:
    print('Invalid option')

