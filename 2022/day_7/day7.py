# {
#     [
#         {"directories":[{"dir1":[{
#             "directories":[{"dir2":[{
#                                     "directories":[], "files":[]
#                                     }]
#                             }],
#             "files":[{"file1":[{"size":0
#                               ,"extension":""}]
#                   ,"file2":[{"size":0
#                              ,"extension":""
#                              }]}]
#         }]}]
#          ,"files":[{"file1":[{"size":0
#                               ,"extension":""}]
#                   ,"file2":[{"size":0
#                              ,"extension":""
#                              }]
#                     }]}
#     ]
# }

file1 = open('day7_input.txt', 'r')
file_line = file1.readlines()

f_s = {}
current_command = ''
current_directory = ''
previous_directory = ''
working_path = ''

folder = {}
file_sizes = {}
current_directory = []
dir_name = []
total_size = 0
p_dir = ''

for line in file_line:
    line = line.strip()
    #print(line[5:len(line)])
    if line.split(' ')[0].isnumeric():
        total_size = total_size + int(line.split(' ')[0])
    if line.startswith('$ cd ..'):
        current_directory.pop()
    else:
        if line.startswith('$ cd'):
            current_directory.append(p_dir + "/" + line.split(' ')[2])
            folder[p_dir + "/" + line.split(' ')[2]] = 0
            p_dir = line.split(' ')[2]
            #folder[str(current_directory)] = 0
        else:
            if line.split(' ')[0] != 'dir' and line[0] != '$':
                for dr in current_directory:
                    folder[dr] = folder[dr] + int(line.split(' ')[0])
    print(line)
    print(current_directory)
    print(folder)
    #input('wait')


    #print(line)
    #print(current_directory)
    #print(folder)

elig_del = 0
print(folder)
for sz in folder:
    if folder[sz] <= 100000:
        elig_del = elig_del + folder[sz]

print(total_size)
print(elig_del)

# 1348005
# part two
unsed = []
print('part 2')
remaining = 70000000 - total_size
print(f'need {remaining}')
for sz_z in folder:
    if folder[sz_z] + remaining >= 30000000:
        print(folder[sz_z])
        unsed.append(folder[sz_z])

print('sorting')
unsed.sort()
print(unsed)

#24933642 too high
#45811471
#45811471