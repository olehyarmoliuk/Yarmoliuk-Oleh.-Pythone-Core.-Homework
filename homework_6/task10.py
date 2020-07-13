names = ('Ann', 'Bob', 'Elizabeth', 'Mr. McMullen', 'Mrs. Smith')
print(names)

for i in names:
    if i[:3] == 'Mr.': 
        print('Good morning,', i)
    elif i[:4] == 'Mrs.':
        print('Good morning,', i)
    else:
        print('Hello,', i)