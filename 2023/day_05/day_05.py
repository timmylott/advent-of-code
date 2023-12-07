file1 = open('day_05_input.txt', 'r')
file_lines = file1.readlines()

for line in file_lines:
    line = line.strip()
    if line.startswith('seeds:'):
        seeds = line.split(':')[1].strip().split(' ')

seed_map_dic = {}

for seed in seeds:
    follow = seed
    in_mapping = False
    source_range = []
    destination_range = []
    map_found = False
    seed_map = {}
    current_convert = ''
    do_not_have_new_follow = True
    for line in file_lines:
        line = line.strip()
        if 'map:' in line:
            current_convert = line.split('-')[2].split(' ')[0]
            in_mapping = True
            do_not_have_new_follow = True

        if in_mapping and line != '' and 'map:' not in line:
            destination_start = line.split(' ')[0]
            source_start = line.split(' ')[1]
            range_length = line.split(' ')[2]

            #  source_range = [*range(int(source_start), int(source_start) + int(range_length))]
            #  destination_range = [*range(int(destination_start), int(destination_start) + int(range_length))]

            if int(source_start) <= int(follow) <= (int(source_start) + int(range_length)) and do_not_have_new_follow:
                # source_seed_index = source_range.index(int(follow))
                # follow = destination_range[source_seed_index]
                follow = int(destination_start) + (int(follow) - int(source_start))
                do_not_have_new_follow = False

        if in_mapping:
            seed_map[current_convert] = int(follow)
            seed_map_dic['Seed ' + seed] = seed_map

        if in_mapping and line == '':
            in_mapping = False

print(seed_map_dic)

lowest_location = []
for seed in seed_map_dic:
    lowest_location.append(seed_map_dic[seed]['location'])

print(min(lowest_location))

# Part Two
import re

file1 = open('day_05_input.txt', 'r')
file_lines = file1.readlines()

seeds = []
seed_map_dic = {}
converter = ''
converter_nbr = {}
converter_nbr_array = []
converter_stack = {}
seed_range = {}
seed_ranges = []
for line in file_lines:
    line = line.strip()
    if 'seeds:' in line:
        seed_pair = re.findall('\d+ \d+', line)
        for pair in seed_pair:
            seed_range['min'] = int(pair.split(' ')[0])
            seed_range['max'] = int(pair.split(' ')[0]) + int(pair.split(' ')[1]) - 1
            seed_ranges.append(seed_range.copy())

        print('seed ranges built')
        print(seed_ranges)
    if 'map:' in line and converter == '':
        converter = line.split(' ')[0]
    if converter != '' and 'map:' not in line and line != '':
        converter_nbr['destination_start'] = int(line.split(' ')[0])
        converter_nbr['source_start'] = int(line.split(' ')[1])
        converter_nbr['range_length'] = int(line.split(' ')[2])
        converter_nbr_array.append(converter_nbr.copy())
        converter_stack[converter] = converter_nbr_array

    if line == '':
        converter_nbr = {}
        converter_nbr_array = []
        converter = ''

print('convert ranges built')
loc = 1
do_not_have_new_follow = True
location_found = False
print('looking for location...')

# Still not the most efficient but working backwards was faster.
# Start with location 1, get seed and then see if seed is within the given ranges, increment and repeat.
while loc != -1:
    follow = loc
    if loc % 100000 == 0:
        print(loc)
    for cnt in reversed(converter_stack):
        for cnt_range in converter_stack[cnt]:
            if cnt_range['destination_start'] <= follow <= (
                    cnt_range['destination_start'] + cnt_range['range_length'] - 1) and do_not_have_new_follow:
                follow = cnt_range['source_start'] + (follow - cnt_range['destination_start'])
                do_not_have_new_follow = False
        do_not_have_new_follow = True

    # check if seed is within seed_ranges
    for rng in seed_ranges:
        if rng['min'] <= follow <= rng['max']:
            print('LOCATION FOUND!')
            print(loc)
            location_found = True
    if location_found:
        break;
    loc = loc + 1
