number = input('Enter a number: ')
sum_of_digits = sum(int(i) for i in str(number))

print(sum_of_digits)
print(number[::-1])
print(sum(int(i) for i in str(number[::-1])))