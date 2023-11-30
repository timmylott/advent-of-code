file1 = open('day1_input.txt', 'r')
file_lines = file1.readlines()

elf_cal_list = []
elf_cal_total = 0
elf_top_three_total = 0

for line in file_lines:
    if line == '\n':
        elf_cal_list.append(elf_cal_total)
        elf_cal_total = 0
    else:
        elf_cal_total = elf_cal_total + int(line.strip())

print(f'Elf {elf_cal_list.index(max(elf_cal_list))+1} has the most calories of {max(elf_cal_list)}')

elf_cal_list.sort(reverse=True)
elf_top_three_total = elf_cal_list[0] + elf_cal_list[1] + elf_cal_list[2]

print(f'Top three elves have total calories of {elf_top_three_total}')