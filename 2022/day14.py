from copy import copy
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]


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


file1 = open('day14_input.txt', 'r')
file_line = file1.readlines()

rocks = []
map = []
t = []

# for rr in range(100):
#    for r in range(600):
#        t.append('.')
#    map.append(copy(t))

for line in file_line:
    line = line.strip()
    current = []
    previous = []
    for c in line.split('->'):
        cor = []
        for cr in c.split(','):
            cor.append(int(cr))
        current = cor
        if len(previous) != 0:
            fill_g = [previous, current]
            fill_g.sort()
            for fl in list(fill_gaps(fill_g)):
                rocks.append(copy(fl))
            previous = current
        else:
            previous = current

max_num = 0
for r in rocks:
    if r[1] > max_num:
        max_num = r[1]

floor = max_num + 2

print(floor)

# add floor
for i in range(10000):
    rocks.append(copy([i, floor]))
# plt.show()
# print(max_num)
# input('wait')
sand = []
sand_number_of = 0
sand_cur = [0, 0]
hit_max = 0
sand_cur_stopped = 0
r = -1

while True:
    r = r + 1
    if sand_cur == [500, 0]:
        break
    if sand_cur[1] > floor:
        print('floor not big enough')
        break
    if sand_number_of % 500 == 0:
        print(sand_number_of)
        print(sand_cur)
    sand_cur = [500, -1]
    while True:
        # if len(sand) == 22:
        #    print('check it out')
        sand_cur[1] = sand_cur[1] + 1
        # if sand_cur[1] > max_num:
        #    hit_max = 1
        #    break
        if [sand_cur[0], sand_cur[1] + 1] in rocks:
            if [sand_cur[0] - 1, sand_cur[1] + 1] in rocks:  # or [sand_cur[0] - 1, sand_cur[1]] in rocks:
                if [sand_cur[0] + 1, sand_cur[1] + 1] in rocks:  # or [sand_cur[0] + 1, sand_cur[1]] in rocks:
                    sand_cur_stopped = 1
                else:
                    sand_cur = [sand_cur[0] + 1, sand_cur[1]]
            else:
                sand_cur = [sand_cur[0] - 1, sand_cur[1]]
        #        else:
        #            if hit_max == 1:
        #                break

        if sand_cur_stopped == 1:
            sand.append(copy(sand_cur))
            rocks.append(copy(sand_cur))
            sand_cur_stopped = 0
            sand_number_of = sand_number_of + 1
            break

#    if hit_max == 1:
#        break

print(sand_number_of)

# part 2 - 28145
