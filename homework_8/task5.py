def is_year_leap(year):
    if year % 4 == 0 and year not in (1700, 1800, 1900, 2100, 2200, 2300):
        return True
    else: 
        return False

userYear = int(input('Enter a year '))
res = is_year_leap(userYear)
print(res)