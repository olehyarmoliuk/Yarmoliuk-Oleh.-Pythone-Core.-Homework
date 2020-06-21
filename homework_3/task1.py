while True:
    try:
        year = int(input('Enter a year '))
        break
    except:
        print('Incorrect value!')

if year % 4 == 0 and year not in (1700, 1800, 1900, 2100, 2200, 2300):
    print('This year is intercalary')
else: 
    print('This year is usual')

if year % 100 == 0:
    print('It is', int(year / 100), 'century')
elif year < 0:
    print('It is', abs(int(year / 100 - 1)), 'century BC')
else: 
     print('It is', int(year / 100 + 1), 'century')