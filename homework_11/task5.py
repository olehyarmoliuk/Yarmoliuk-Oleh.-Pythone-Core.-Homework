file = open("task5_1.txt", "r")
file_output = open("text_output.txt", "a")
lines = file.readlines()

first_str = lines[0]
second_str = lines[1]

a = set(first_str)
b = set(second_str)

set_both = b.intersection(a)
file_output.write('\n''')
file_output.write('\nResults of task 5:')
file_output.write(f'\nCommon element(s) in both sets are: {set_both}')

set_diff_1 = a.difference(b)
set_diff_2 = b.difference(a)

if len(set_diff_1) > 0:
    file_output.write(f'\nFirst set has such unique elements: {set_diff_1}')
else: 
    file_output.write(f'\nFirst set has no unique elements!')

if len(set_diff_2) > 0:
    file_output.write(f'\nSecond set has such unique elements: {set_diff_2}')
else:
    file_output.write(f'\nSecond set has no unique elements!')

file.close()
file_output.close()