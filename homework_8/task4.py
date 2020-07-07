def is_prime(number):
    if number == 1: 
        return False
    elif number == 2:
        return True
    else:
        for d in range(2, number):
            if number % d == 0:
                return False
        return True
    

n = int(input('Enter a number '))
res = is_prime(n)

if res == True:
    print(res, '\nYour number is prime')
else:
    print(res, '\nYour number is composite')