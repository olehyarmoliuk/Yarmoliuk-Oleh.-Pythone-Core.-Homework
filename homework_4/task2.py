mult_5 = 0
for i in range(1, 11):
   num_1 = int(input('Enter a number '))
     
   if  num_1 % 5 == 0:
      mult_5 += 1
      print(num_1, 'multiples of 5')

print(mult_5, 'numbers multiples of 5')