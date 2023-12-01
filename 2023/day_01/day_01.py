import re

file1 = open('day_01_input.txt', 'r')
file_lines = file1.readlines()

calibration_sum = 0

for line in file_lines:
    calibration_sum = calibration_sum + int(re.search(r'\d', line).group() + re.search(r'\d', line[::-1]).group())

print(calibration_sum)

# part two

file1 = open('day_01_input.txt', 'r')
file_lines = file1.readlines()

number_map = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
calibration_sum = 0
sort_replace = {}

for line in file_lines:
    for x in range(0, len(line)):
        if line[x].isnumeric():
            sort_replace[x] = line[x]

    for nbr in number_map:
        indexes = [w.start() for w in re.finditer(nbr, line)]
        for x in indexes:
            sort_replace[x] = number_map[nbr]

    sort_replace = dict(sorted(sort_replace.items()))

    calibration_sum = calibration_sum + int(sort_replace[min(sort_replace)] + sort_replace[max(sort_replace)])
    sort_replace = {}

print(calibration_sum)








