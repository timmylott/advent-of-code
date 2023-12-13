file1 = open('day_08_input.txt', 'r')
file_lines = file1.readlines()

map = {}
move = {}
cord = {}
direction = ''

start = 'AAA'
stop = 'ZZZ'

for line in file_lines:
    line = line.strip()
    if '=' not in line and line != '':
        direction = line
    if '=' in line:
        cord['L'] = line.split('=')[1].split(',')[0].replace('(','').replace(')','').strip()
        cord['R'] = line.split('=')[1].split(',')[1].replace('(', '').replace(')', '').strip()
        map[line.split('=')[0].strip()] = cord
        move = {}
        cord = {}

steps = 0
multi = 1
loc = 0

while loc != -1:
    if (loc) == len(direction):
        direction = direction + direction

    i = direction[loc]

    start = map[start][i]
    steps = steps + 1
    if start == 'ZZZ':
        print('at the end')
        break;
    loc = loc + 1

print(steps)

# part 2

file1 = open('day_08_input.txt', 'r')
file_lines = file1.readlines()

loc = 0
starting_pos = []
current_pos = {}
pos = {}
move = {}
cord = {}
all_contain_z = False
next_move_starting_pov = []
steps = 0

for line in file_lines:
    line = line.strip()
    if '=' not in line and line != '':
        direction = line
    if '=' in line:
        if line[2] == 'A':
            starting_pos.append(line.split('=')[0].strip())

        cord['L'] = line.split('=')[1].split(',')[0].replace('(','').replace(')','').strip()
        cord['R'] = line.split('=')[1].split(',')[1].replace('(', '').replace(')', '').strip()
        map[line.split('=')[0].strip()] = cord
        move = {}
        cord = {}

print(starting_pos)
while loc != -1:
    if (loc) == len(direction):
        direction = direction + direction
    i = direction[loc]

    for s in starting_pos:
        movement = map[s][i]
        current_pos['pos'] = movement[-1]
        pos[s] = current_pos
        next_move_starting_pov.append(movement)
        if movement[-1] != 'Z':
            all_contain_z = False

    steps = steps + 1

    if all_contain_z:
        print('all end in z')
        break;
    else:
        starting_pos = next_move_starting_pov
        next_move_starting_pov = []
        all_contain_z = True

    loc = loc + 1
print(steps)


