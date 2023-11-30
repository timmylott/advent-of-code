file1 = open('day10_input.txt', 'r')
file_line = file1.readlines()

x = 1
cycle = 0
v = 0

signal_strength = []

for line in file_line:
    line = line.strip()
    instruct = line.split(' ')[0]

    if instruct == 'addx':
        for c in range(2):
            cycle += 1
            if cycle == 20:
                signal_strength.append(cycle * x)
            else:
                if (cycle - 20) % 40 == 0:
                    signal_strength.append(cycle * x)
            if c == 1:
                v = int(line.split(' ')[1])
                x = x + v

    else:
        cycle += 1
        if cycle == 20:
            signal_strength.append(cycle * x)
        else:
            if (cycle - 20) % 40 == 0:
                signal_strength.append(cycle * x)print(x)
print(signal_strength)
print(sum(signal_strength))
#14520
