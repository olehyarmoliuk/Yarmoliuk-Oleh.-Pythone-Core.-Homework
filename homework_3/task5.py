amountMoney = int(input('How much money do you have? '))


if amountMoney > 200:
    print((amountMoney // 200), '- 200 UAH', '|', ((amountMoney % 200) // 100), '- 100 UAH ', '|', 
    ((amountMoney % 100) // 10), '- 10 UAH', '|', ((amountMoney % 100) % 10), '- 1 UAH')
elif 100 < amountMoney < 200:
    print((amountMoney // 100), '- 100 UAH', '|', (amountMoney % 100) // 10, '- 10 UAH ', '|', 
    ((amountMoney % 100)) % 10 , '- 1 UAH')
elif 10 < amountMoney < 100:
    print((amountMoney // 10), '- 10 UAH', '|', (amountMoney % 10), '- 1 UAH')
elif 0 < amountMoney < 10:
    print((amountMoney // 1), '- 1 UAH')
else:
    print('You have no money')