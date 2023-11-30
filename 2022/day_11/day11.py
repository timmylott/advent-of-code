import math
import numpy

file1 = open('day11_input.txt', 'r')
file_line = file1.readlines()

monkey_items = []
monkey_operation = []
monkey_div = []
monkey_throw = [] #0 place who throw when true, 1 place who throw when false
cal = ''
monkey_inspect = []

# Load monkeys
for line in file_line:
    line = line.strip()
    if line.startswith('Starting items:'):
        monkey_items.append(line.split(':')[1].split(","))

    if line.startswith('Operation:'):
        monkey_operation.append(line.split(':')[1].split('=')[1].strip())
    if line.startswith('Test:'):
        monkey_div.append(int(line.split(':')[1].split( ' ')[3]))
    if line.startswith('If true:'):
        throw = []
        throw.append(line.split(':')[1].split(' ')[4])
    if line.startswith('If false:'):
        throw.append(line.split(':')[1].split(' ')[4])
        monkey_throw.append(throw)

for m in monkey_items:
    monkey_inspect.append(0)

for r in range(20):
    for m in range(len(monkey_items)):
        for i in monkey_items[m]:
            cal = monkey_operation[m].replace('old',i)
            if math.floor(eval(cal)/3) % int(monkey_div[m]) == 0:
                monkey_items[int(monkey_throw[m][0])].append(str(math.floor(eval(cal)/3)))
            else:
                monkey_items[int(monkey_throw[m][1])].append(str(math.floor(eval(cal)/3)))
            monkey_inspect[m] = monkey_inspect[m] + 1
        monkey_items[m] = []


print(monkey_items)
print(monkey_operation)
print(monkey_div)
print(monkey_throw)
monkey_inspect.sort(reverse=True)

print(monkey_inspect[0] * monkey_inspect[1])
#110888


