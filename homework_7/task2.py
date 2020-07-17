first_str = input('Enter a sentence ')
second_str = input('Enter a sentence ')

a = set(first_str)
b = set(second_str)

set_both = b.intersection(a)
print('Common element(s) in both sets are:', set_both)

set_diff_1 = a.difference(b)
set_diff_2 = b.difference(a)

if len(set_diff_1) > 0:
    print('First set has such unique elements:', set_diff_1)
else: 
    print('First set has no unique elements!')

if len(set_diff_2) > 0:
    print('Second set has such unique elements:', set_diff_2)
else:
    print('Second set has no unique elements!')