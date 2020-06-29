sen_1 = input("Enter a sentence ")
num_spaces = 0

for i in sen_1:
    if (i.isspace()) == True:
        num_spaces += 1
print(num_spaces)