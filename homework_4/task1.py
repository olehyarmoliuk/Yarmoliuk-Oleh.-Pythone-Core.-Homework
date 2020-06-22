import random

attempts = 0
number = random.randint(0, 100)

while attempts < 10:
    guess = int(input('guess a number from 0 to 100 '))
    attempts += 1

    if 0 > guess or guess > 100 :
        print('Read rules attentively!!! You have only', 10 - attempts, 'attempts left!')
        continue
        
    if guess < number:
        print('bigger')
    elif guess > number:
        print('smaller')
    else: 
        guess == number
        print('You guessed! It took only', attempts, 'attempts!')
        break
           
    
if guess != number:
    print('You lose... The number is', number)