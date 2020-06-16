while True:
    try:
        year = int(input('Enter a year '))
        break
    except:
        print('Incorrect value!')

if year % 4 == 0:
    print('This year is intercalary')
elif year % 4 != 0:
    print('This year is usual')
print('It is', int(year / 100 + 1), 'century')