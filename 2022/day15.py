import re
from copy import copy


def fill_gaps(coordinates):
    last_x, last_y = None, None

    for x, y in coordinates:
        if y == last_y:
            # Fill in any potential gaps between the last value and us
            yield from ([new_x, y] for new_x in range(last_x + 1, x))

        if x == last_x:
            # Fill in any potential gaps between the last value and us
            yield from ([x, new_y] for new_y in range(last_y + 1, y))

        last_x, last_y = x, y
        yield [x, y]


file1 = open('day15_input.txt', 'r')
file_line = file1.readlines()

map_sb = []
all_bb = []

for line in file_line:
    s = []
    b = []
    line = line.strip()
    ss = re.search('Sensor at x=(.*), y=(.*):.*', line)
    bb = re.search('.*closest beacon is at x=(.*), y=(.*)', line)
    s = [int(ss.group(1)), int(ss.group(2))]
    b = [int(bb.group(1)), int(bb.group(2))]
    all_bb.append(copy(b))
    dis = abs(int(s[0]) - int(b[0])) + abs(int(s[1]) - int(b[1]))
    print(f'distance: {dis}')
    for a in range(dis + 1):
        map_sb.append(copy([int(s[0]) + a, int(s[1])]))
        fill_g = [[int(s[0]) + a, s[1]], [int(s[0]) + a, int(s[1]) + (dis - a)]]
        fill_g.sort()
        for fl in list(fill_gaps(fill_g)):
            map_sb.append(copy(fl))
    print('after a')
    for b in range(dis + 1):
        map_sb.append(copy([int(s[0]) - b, int(s[1])]))
        fill_g = [[int(s[0]) - b, s[1]], [int(s[0]) - b, int(s[1]) + (dis - b)]]
        fill_g.sort()
        for fl in list(fill_gaps(fill_g)):
            map_sb.append(copy(fl))
    print('after b')
    for c in range(dis + 1):
        map_sb.append(copy([int(s[0]), int(s[1]) - c]))
        fill_g = [[int(s[0]), s[1] - c], [int(s[0]) - (dis - c), int(s[1]) - c]]
        fill_g.sort()
        for fl in list(fill_gaps(fill_g)):
            map_sb.append(copy(fl))
    print('after c')
    for d in range(dis + 1):
        map_sb.append(copy([int(s[0]), int(s[1]) + d]))
        fill_g = [[int(s[0]), s[1] - d], [int(s[0]) + (dis - d), int(s[1]) - d]]
        fill_g.sort()
        for fl in list(fill_gaps(fill_g)):
            map_sb.append(copy(fl))
    print('after d')
    print(line)

map_cnt = []
for m in map_sb:
    if m[1] == 2000000:
        if m not in map_cnt and m not in all_bb:
            map_cnt.append(copy(m))

print(f'the len is {len(map_cnt)}')
