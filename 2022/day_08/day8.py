file1 = open('day8_input.txt', 'r')
file_line = file1.readlines()

grid = []
columns = []
visable_total = 0

for line in file_line:
    line = line.strip()
    row = []
    for t in line:
        row.append(t)
    grid.append(row)

columns = list(zip(*grid))

for g in range(len(grid)):
    for t in range(len(grid[g])):
        if g == 0 or g == len(grid) - 1 or t == 0 or t == len(grid[g]) - 1:  # outside edge
            visable_total = visable_total + 1
        else:
            if grid[g][t] > max(grid[g][t + 1:len(grid[g])]) or \
                    grid[g][t] > max(grid[g][0:t]) or \
                    grid[g][t] > max(columns[t][g + 1:len(columns[t])]) or \
                    grid[g][t] > max(columns[t][0:g]):
                visable_total = visable_total + 1

print(visable_total)
# 1825

highest_scenic_score = 0

print('part two')
for g in range(len(grid)):
    for t in range(len(grid[g])):

        if g == 0 or g == len(grid) - 1 or t == 0 or t == len(grid[g]) - 1:  # outside edge
            outside_edge = 0
        else:
            print(f'current value {grid[g][t]}')
            up_score = 0
            #grid[g][t] > max(columns[t][0:g])
            for u in range(g-1, -1, -1):
                if grid[u][t] <= grid[g][t] or grid[u][t] > grid[g][t]:
                    up_score = up_score + 1
                    if grid[u][t] >= grid[g][t]:
                        break

            print(f'up {up_score}')

            down_score = 0
            #max(columns[t][g+1:len(columns[t])])
            for d in range(g+1, len(columns[t])):
                if grid[d][t] <= grid[g][t] or grid[d][t] > grid[g][t]:
                    down_score = down_score + 1
                    if grid[d][t] >= grid[g][t]:
                        break

            print(f'down {down_score}')

            left_score = 0
            #grid[g][t] > max(grid[g][0:t])
            for l in range(t-1, -1, -1):
                if grid[g][l] <= grid[g][t] or grid[g][l] > grid[g][t]:
                    left_score = left_score + 1
                    if grid[g][l] >= grid[g][t]:
                        break

            print(f'left {left_score}')

            right_score = 0
            #max(columns[t][g+1:len(columns[t])])
            for r in range(t+1, len(grid[g])):
                if grid[g][r] <= grid[g][t] or grid[g][r] > grid[g][t]:
                    right_score = right_score + 1
                    if grid[g][r] >= grid[g][t]:
                        break

            print(f'right {right_score}')

            if (up_score * down_score * left_score * right_score) > highest_scenic_score:
                highest_scenic_score = up_score * down_score * left_score * right_score

            print(f'high score {highest_scenic_score}')
            #input('wait')

print(highest_scenic_score)
#235200
