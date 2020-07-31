input_data = open("task4_1.txt", "r")
data_read = input_data.read()
output_data = open("text_output.txt", "a")

output_data.write('\n''')
output_data.write(f'\nResults of task 4:')
output_data.write(f'\n{data_read.replace(" ", "_")}')

input_data.close()
output_data.close()