file1 = open('day10_input.txt', 'r')
file_line = file1.readlines()

x = 1
cycle = 0
cycle_2 = 0
v = 0

signal_strength = []
crt = []
sprite = ['........................................']
row = '........................................'
sprite_pos = 1

for line in file_line:
    line = line.strip()
    instruct = line.split(' ')[0]

    if instruct == 'addx':
        for c in range(2):
            if sprite_pos - 1 <= cycle_2 <= sprite_pos + 1:
                row = row[:cycle_2] + '#' + row[cycle_2 + 1:]
            cycle += 1
            cycle_2 += 1

            if cycle == 20:
                signal_strength.append(cycle * x)
                # crt.append(row)
            else:
                if (cycle - 20) % 40 == 0:
                    signal_strength.append(cycle * x)
                if cycle % 40 == 0:
                    crt.append(row)
                    cycle_2 = 0
                    row = '........................................'
            if c == 1:
                v = int(line.split(' ')[1])
                x = x + v
                sprite_pos = x

    else:
        if sprite_pos - 1 <= cycle_2 <= sprite_pos + 1:
            row = row[:cycle_2] + '#' + row[cycle_2 + 1:]
        cycle += 1
        cycle_2 += 1
        if cycle == 20:
            signal_strength.append(cycle * x)
            # crt.append(row)
        else:
            if (cycle - 20) % 40 == 0:
                signal_strength.append(cycle * x)
            if cycle % 40 == 0:
                crt.append(row)
                cycle_2 = 0
                row = '........................................'

for l in crt:
    print(l)

#PZBGZEJB