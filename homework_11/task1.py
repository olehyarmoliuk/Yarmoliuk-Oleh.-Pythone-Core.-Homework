def calculator(arg):
    def sum(a, b):
        return a + b
    def dif(a, b):
        return a - b
    def product(a, b):
        return a * b
    def fraction(a, b):
        return a / b

    if arg == 1: 
        return sum
    elif arg == 2:
        return dif
    elif arg == 3:
        return product
    elif arg == 4:
        return fraction
    else: 
        print('You can choose only 1-4')

while True:
    try:
        choice = int(input('Choose an operation: \n1. To sum numbers \n2. To subtract numbers \n3. To multiply numbers \
        \n4. To divide numbers \n5. Press "0" to exit '))
        if choice in range(1, 5):
            result_1 = calculator(choice)
            a = int(input('Choose first number '))
            b = int(input('Choose second number '))
            print(f'The result is {result_1(a, b)}.')
        elif choice == 0:
            print('Good bye!')
            break
        else:
            print('Something went wrong. Please, try again.')
            choice
    except ValueError:
        print('Please, enter a digit.')
    except Exception:
        print('It seems to me you made a mistake!')