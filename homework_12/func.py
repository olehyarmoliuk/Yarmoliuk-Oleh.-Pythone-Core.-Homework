def product(a, b):
    return a * b

def encrypt(string, key):
    cipher = ''
    for char in string: 
        if char == ' ':
            cipher = cipher + char
        elif  char.isupper():
            cipher = cipher + chr((ord(char) + key - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + key - 97) % 26 + 97)
    return cipher


def key_occur(str):
    count = dict()
    words = str.split()
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count


def arithTask(*args):
    if len(args) == 0: return 0
    if len(args) > 3: return print('Incorrect input')
    if args[2] == '+': return args[0] + args[1]
    if args[2] == '-': return args[0] - args[1]
    if args[2] == '*': return args[0] * args[1]
    if args[2] == '/': return args[0] / args[1]

def is_prime(number):
    if number == 1: 
        return False
    elif number == 2:
        return True
    else:
        for d in range(2, number):
            if number % d == 0:
                return False
        return True