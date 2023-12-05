import re

file1 = open('day_03_input_sample.txt', 'r')
file_lines = file1.readlines()


for line in file_lines:
    line = line.strip()
    print(line)
    print(line.split('.'))
    print(re.findall('\d+', line))