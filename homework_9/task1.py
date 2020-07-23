import random

class Pond:
    def __init__(self, capacity=0, state='poor'):
        self.capacity = capacity
        self.state = state
            
    def obtainFish(self):
        self.capacity = (self.capacity + 1)
        return self.capacity
    
    def lostFish(self):
        self.capacity = (self.capacity - 1)
        return self.capacity
    
    def showCapacity(self):
        return f'There are {self.capacity} fish in the pond at the moment.'
    
    def showState(self):
        if 0 <= self.capacity < 5:
            self.state = 'poor'
        elif 5 <= self.capacity <= 10:
            self.state = 'normal'
        else:
            if self.capacity > 10:
                self.state = 'rich'
        return f"The pond's state is {self.state} now."

class Fish:
    def __init__(self, weight):
        self.weight = weight
    
    def fish_weight(self):
        return self.weight

class SheatFish (Fish):
    def length_whisk(self, whiskerLength=0):
        self.whiskerLength = whiskerLength
        return self.whiskerLength

class Carp (Fish):
    def color_carp(self, color=''):
        self.color = color
        return self.color

menu = '''1. View capacity \n2. View state of Pond \n3. Add fish (carp or sheatfish) \
\n4. Catch fish (concrete one) \n5. Create new fish \n6. Finish the game \n7. Show menu'''
print('%12s' %('MENU'))
print(menu)

fish_game = Pond()
fish_list = {'Sheatfish': 0, 'Carp': 0}

while True:
    try:
        choice = int(input('Choose option "1-6" or press "7" to show menu '))
        if choice == 1:
            print(fish_game.showCapacity(), f'These are {fish_list}')
        elif choice == 2:
            print(fish_game.showState())
        elif choice == 3:
            fish_choice = int(input('What fish would you like to add: 1. a sheatfish or 2. a carp? '))
            if fish_choice == 1:
                fish_game.obtainFish()
                fish_list['Sheatfish'] += 1
                print(fish_list) 
            else:
                if fish_choice == 2:
                    fish_game.obtainFish()
                    fish_list['Carp'] += 1
                    print(fish_list)
        elif choice == 4:
            Sheatfish = SheatFish(round((random.uniform(0.25, 20)), 2))
            Carp_1 = Carp(round((random.uniform(0.25, 5)), 2))
            if fish_game.capacity <= 0:
                print('You have no fish already ')
                int(input('Press "3" to add a new one '))
            print(f"There are {fish_list} in the pond.")
            fish_catch = int(input('What fish do you like to catch: 1. a sheatfish or 2. a carp? '))
            if fish_catch == 1:
                fish_game.lostFish()
                fish_list['Sheatfish'] -= 1
                print(f"You have successfully catched the sheatfish! It's weight is {Sheatfish.fish_weight()} kg" + 
                f" and length of its whiskers is {Sheatfish.length_whisk(round((random.uniform(5, 20)), 2))} cm.") 
                if fish_list['Sheatfish'] <= 0:
                    fish_list['Sheatfish'] = 0
                    print('There is no sheatfish already')
            else:
                if fish_catch == 2:
                    fish_game.lostFish()
                    fish_list['Carp'] -= 1
                    print(f"You have successfully catched the carp! It's weight is {Carp_1.fish_weight()} kg" + 
                    f" and its color is {Carp_1.color_carp('dark brown')}.") 
                    if fish_list['Carp'] <= 0:
                        fish_list['Carp'] = 0
                        print('There is no carp already')  
        elif choice == 5:
            new_choice = int(input('You can create a new fish! Is it subspecies of 1. a sheatfish or 2. a carp? '))
            if new_choice == 1:
                fish_1 = input('How would you name it? ')
                fish_game.obtainFish()
                fish_list['Sheatfish'] += 1
                new_fish_1 = SheatFish(round((random.uniform(0.25, 25)), 2))
                print(f"You have successfully created the {fish_1}: its weigth - {new_fish_1.fish_weight()} kg," +
                f" whiskers length - {new_fish_1.length_whisk(round((random.uniform(7, 15)), 2))} cm")
            else:
                if new_choice == 2:
                    fish_2 = input('How would you name it? ')
                    fish_game.obtainFish()
                    fish_list['Carp'] += 1
                    new_fish_2 = Carp(round((random.uniform(0.25, 25)), 2))
                    print(f"You have successfully created the {fish_2}: its weigth - {new_fish_2.fish_weight()} kg," +
                    f" color - {new_fish_2.color_carp('golden brown')}")
        elif choice == 6:
            print('Good bye!')
            break
        elif choice == 7:
            print('%12s' %('MENU'))
            print(menu)
        else:
            print('There is no such option!')
    except Exception:
        print('Incorrect value!')