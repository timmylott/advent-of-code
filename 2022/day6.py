file1 = open('day6_input.txt', 'r')
file_line = file1.readline()

length_of_start = 14

for input_num in range(len(file_line)):
    if len(set(file_line[input_num:input_num+length_of_start])) == length_of_start:
        print(f'first marker: {input_num + length_of_start}')
        break
