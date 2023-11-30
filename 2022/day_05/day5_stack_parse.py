file1 = open('day5_input_stack.txt', 'r')
file_lines = file1.readlines()

resort_stack = []
stacks = []
stack = []

for line in file_lines:
    line = line.strip()
    if line[0] == '1':
        number_of_stacks = line.replace(' ','')
        break
    resort_stack.insert(0, '   ' + line)

for stack_num in number_of_stacks:
    stack = []
    for line in resort_stack:
        if len(line) >= 4 * int(stack_num) and line[4 * int(stack_num)] != ' ':
            stack.append(line[4 * int(stack_num)])
    stacks.append(stack)

for s in stacks:
    print(s)





