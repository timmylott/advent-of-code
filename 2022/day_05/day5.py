#  [J]             [F] [M]
#  [Z] [F]     [G] [Q] [F]
#  [G] [P]     [H] [Z] [S] [Q]
#  [V] [W] [Z] [P] [D] [G] [P]
#  [T] [D] [S] [Z] [N] [W] [B] [N]
#  [D] [M] [R] [J] [J] [P] [V] [P] [J]
#  [B] [R] [C] [T] [C] [V] [C] [B] [P]
#  [N] [S] [V] [R] [T] [N] [G] [Z] [W]
#   1   2   3   4   5   6   7   8   9

stack = [['N','B','D','T','V','G','Z','J']
        , ['S','R','M','D','W','P','F']
        , ['V','C','R','S','Z']
        , ['R','T','J','Z','P','H','G']
        , ['T','C','J','N','D','Z','Q','F']
        , ['N','V','P','W','G','S','F','M']
        , ['G','C','V','B','P','Q']
        , ['Z','B','P','N']
        , ['W','P','J']]

file1 = open('day5_input.txt', 'r')
file_lines = file1.readlines()

for line in file_lines:
    line = line.strip()
    instruct = line.split(' ')
    instruct_quantity = int(instruct[1])
    instruct_from = int(instruct[3]) - 1
    instruct_to = int(instruct[5]) - 1

    for i in range(instruct_quantity):
        stack[instruct_to].append(stack[instruct_from][len(stack[instruct_from])-i-1])
    del stack[instruct_from][len(stack[instruct_from])-instruct_quantity:len(stack[instruct_from])]

print('Part 1 final stack config')
for st in stack:
    print(st)

print('END PART 1')
print('START PART 2')

stack = [['N','B','D','T','V','G','Z','J']
        , ['S','R','M','D','W','P','F']
        , ['V','C','R','S','Z']
        , ['R','T','J','Z','P','H','G']
        , ['T','C','J','N','D','Z','Q','F']
        , ['N','V','P','W','G','S','F','M']
        , ['G','C','V','B','P','Q']
        , ['Z','B','P','N']
        , ['W','P','J']]

for line in file_lines:
    line = line.strip()
    instruct = line.split(' ')
    instruct_quantity, instruct_from, instruct_to = int(instruct[1]), int(instruct[3]) - 1, int(instruct[5]) - 1

    for index, item in list(enumerate(stack[instruct_from])):
        if index >= len(stack[instruct_from]) - instruct_quantity:
            stack[instruct_to].append(item)
    del stack[instruct_from][len(stack[instruct_from])-instruct_quantity:len(stack[instruct_from])]

print('Part 2 final stack config')
for st in stack:
    print(st)