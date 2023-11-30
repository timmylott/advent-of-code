file1 = open('2021_day3_input.txt', 'r')
file_lines = file1.readlines()
#cnt = file1.readline()
bn = []
gama = ''
epsilon = ''

for cnt in range(len(file_lines[0].strip())):
    for line in file_lines:
        line = line.strip()
        bn.append(line[cnt])
    if bn.count('0') > bn.count('1'):
        gama = gama + '0'
        epsilon = epsilon + '1'
    else:
        gama = gama + '1'
        epsilon = epsilon + '0'
    bn = []

print(int(gama, 2))
print(int(epsilon, 2))
print(int(gama, 2) * int(epsilon, 2))


#part 2
bn = []
gama = ''
epsilon = ''

for cnt in range(len(file_lines[0].strip())):
    for line in file_lines:
        line = line.strip()
        bn.append(line[cnt])
    if bn.count('0') > bn.count('1'):
        gama = gama + '0'
        epsilon = epsilon + '1'
    else:
        gama = gama + '1'
        epsilon = epsilon + '0'
    bn = []


