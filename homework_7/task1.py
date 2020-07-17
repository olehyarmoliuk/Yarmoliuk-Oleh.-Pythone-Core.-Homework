arith_signs = ['+', '-', '*', '/', '%', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

str_1 = input('Enter a string ')
str_new = ''
for i in range(len(str_1)):
    if str_new.find(str_1[i]) == -1 and str_1[i] != ' ' and str_1[i] in arith_signs:
        str_new += str_1[i]
    else: 
        if str_1[i] not in arith_signs:
            str_new += str_1[i]
print(f'New string without repetitions of numbers is {str_new}')