def arithTask(*args):
    if len(args) == 0: return 0
    if len(args) > 3: return print('Incorrect input')
    if args[2] == '+': return args[0] + args[1]
    if args[2] == '-': return args[0] - args[1]
    if args[2] == '*': return args[0] * args[1]
    if args[2] == '/': return args[0] / args[1]

num_1 = int(input('Enter the first number '))
num_2 = int(input('Enter the second number '))
oper_1 = input('Choose an operator ')

res = arithTask(num_1, num_2, oper_1)
print(res)