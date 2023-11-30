file1 = open('day4_input.txt', 'r')
file_lines = file1.readlines()
full_contains_total = 0
full_contains_overlap_count = 0

#for line in file_lines:
#    line = line.strip()
#    print(line)
#    section = line.split(',')
#    section_one_range = section[0].split('-')
#    section_two_range = section[1].split('-')
#    print(section_one_range)
#    print(section_two_range)
#    if (int(section_one_range[0]) >= int(section_two_range[0]) and int(section_one_range[1]) <= int(section_two_range[1])) \
#            or (int(section_two_range[0]) >= int(section_one_range[0]) and int(section_two_range[1]) <= int(section_one_range[1])):
#        full_contains_total = full_contains_total + 1
#
#print(full_contains_total)
#359 wrong, too high

#part two
for line in file_lines:
    line = line.strip()
    section = line.split(',')
    section_one_range = section[0].split('-')
    section_two_range = section[1].split('-')

    one_range = range(int(section_one_range[0]),int(section_one_range[1])+1)
    two_range = range(int(section_two_range[0]),int(section_two_range[1])+1)

    if set(one_range).intersection(two_range):
        full_contains_overlap_count = full_contains_overlap_count + 1

print(full_contains_overlap_count)
#811