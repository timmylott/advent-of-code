file1 = open('day_09_input_sample.txt', 'r')
file_lines = file1.readlines()

seq_a = []
pre = 0
stack = []

for line in file_lines:
    line = line.strip()
    seq = line.split(' ')
    print(seq)
    for i in range(len(seq)-1):
        print(i)
        seq_a.append(int(seq[i+1])-int(seq[i]))
    stack
    print(seq_a)
    seq_a = []

