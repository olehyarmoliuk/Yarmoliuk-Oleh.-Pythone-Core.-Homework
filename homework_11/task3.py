pos_num, neg_num = 0, 0

input_data = open("Homework\Homework_11\task3_1.txt", "r")
output_data = open("text_output.txt", "a")
n = input_data.read()
n_int = [int(x) for x in n.split()]
    
for elem in n_int:
    if elem > 0:
        pos_num += 1
    else: 
        neg_num += 1

per = 100/(pos_num + neg_num)

output_data.write('\n''')
output_data.write('\nResults of task 3:')
output_data.write('\n'f"Percentage of positive numbers: {float(pos_num * per)}")
output_data.write('\n'f"Percentage of negative numbers: {float(neg_num * per)}")

input_data.close()
output_data.close()