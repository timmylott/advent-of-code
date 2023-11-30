import string

file1 = open('day3_input.txt', 'r')
file_lines = file1.readlines()

# Generate lowercase Mapping
letter_value = {chr(l+96):l for l in range(1,27)}

both_compartment_sum = 0

#for line in file_lines:
#    line = line.strip()
#    line_length = len(line)
#    compartment_one, compartment_two = line[:len(line)//2], line[len(line)//2:]
#
#    for item_one in compartment_one:
#        if item_one in compartment_two:
#            if item_one.isupper():
#                both_compartment_sum = both_compartment_sum + letter_value[item_one.lower()] + 26
#            else:
#                both_compartment_sum = both_compartment_sum + letter_value[item_one.lower()]
#            break;
#
#print(both_compartment_sum)
# 7967

priority_sum = 0
group = []
line_num = 1
#part two
for line in file_lines:
    line = line.strip()
    if line_num%3 == 0:
        group.append(line)
        for item_type in group[0]:
            if item_type in group[1] and item_type in group[2]:
                priority_sum = priority_sum + letter_value[item_type.lower()]
                if item_type.isupper():
                    priority_sum = priority_sum + 26
                group = []
                break;
    else:
        group.append(line)
    line_num = line_num + 1

print(priority_sum)
#2716

