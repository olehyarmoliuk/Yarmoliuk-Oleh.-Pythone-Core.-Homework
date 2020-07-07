def depo_func(*args):
    return (args[0] / args[1] * args[2])

amountMoney = int(input('What is your amount of money? '))
years = int(input('For how many years do you want to make a deposit? '))
sum = depo_func(amountMoney, 10, years)
print('You will get', sum, 'in', years, 'years')
print('The total amount of money will be', amountMoney + sum)