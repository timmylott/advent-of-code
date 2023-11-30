file1 = open('2021_day2_input.txt', 'r')
file_lines = file1.readlines()

hoz_pos = 0
depth = 0
aim = 0

for line in file_lines:
    line = line.strip()
    instruct = line.split(' ')
    if instruct[0] in {'up', 'down'}:
        if instruct[0] == 'down':
            depth = depth + int(instruct[1])
        else:
            depth = depth - int(instruct[1])
    else:
        hoz_pos = hoz_pos + int(instruct[1])

print(hoz_pos)
print(depth)
print(hoz_pos*depth)
#6159656 to high
#-6159656

#part two
hoz_pos = 0
depth = 0
aim = 0


for line in file_lines:
    line = line.strip()
    instruct = line.split(' ')
    if instruct[0] in {'up', 'down'}:
        if instruct[0] == 'down':
            aim = aim + int(instruct[1])
        else:
            aim = aim - int(instruct[1])
    else:
        hoz_pos = hoz_pos + int(instruct[1])
        depth = depth + (aim * int(instruct[1]))

print(hoz_pos)
print(depth)
print(hoz_pos*depth)