def date_func(day, month, year):
    
    if month in range(1, 8, 2) or month in range(8, 13, 2):
        if 0 < day < 32:
            return True
        else:
            day > 32    
            return False
    elif month in range(4, 7, 2) or month in range(9, 12, 2):
        if 0 < day < 31:
            return True
        else: 
            day >= 31
            return False
    elif month == 2 and year % 4 == 0 and year not in (1700, 1800, 1900, 2100, 2200, 2300):
        if day <= 29:
            return True
        else: 
            return False
    else:
        return False
    
day = int(input('Enter a day '))
month = int(input('Enter a month '))
year = int(input('Enter a year ')) 

date = date_func(day, month, year)
print(date)

if date == False:
    print('You entered incorrect date!')
else:
    print('Your date is', '{}.{}.{}'.format(day, month, year))