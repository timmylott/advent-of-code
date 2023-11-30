file1 = open('day9_input_test.txt', 'r')
file_line = file1.readlines()

h = [0, 0]
t = [0, 0]
visited = []
v = []

row = 4
column = 0


def show_board(h, t):
    board = [
        ['......'],
        ['......'],
        ['......'],
        ['......'],
        ['......']
    ]
    row = board[h[0]][0]
    board[h[0]][0] = row[:h[1]] + 'H' + row[h[1] + 1:]
    row = board[t[0]][0]
    board[t[0]][0] = row[:t[1]] + 'T' + row[t[1] + 1:]
    board.reverse()
    for r in board:
        print(r)


def is_t_touch(h, t):
    if t[0] in (h[0] - 1, h[0] + 1, h[0]) and t[1] in (h[1] - 1, h[1] + 1, h[1]):
        return True
    else:
        return False


def need_diag_move(h, t):
    if t[0] == h[0] or t[1] == h[1]:
        return False
    else:
        return True


def move_t_diag(hh, tt, dd, mm):
    # same row or colunn
    if tt[0] == hh[0] or tt[1] == hh[1]:
        return tt
    else:  # diag move

#        if dd == "U":
#            tt[0] = tt[0] + 1
#            tt[1] = tt[1] + (hh[1] - tt[1])
#        if dd == 'D':
#            tt[0] = tt[0] - 1
#            tt[1] = tt[1] + (hh[1] - tt[1])
#        if dd == "R":
#            tt[1] = tt[1] + 1
#            tt[0] = tt[0] + (hh[0] - tt[0])
#        if dd == 'L':
#            tt[1] = tt[1] - 1
#            tt[0] = tt[0] + (hh[0] - tt[0])
#        return tt
        x_dist = (hh[0] - tt[0])
        y_dist = (hh[1] - tt[1])
        if x_dist > 1:
            tt[0] += 1
            if y_dist > 0:
                tt[1] += 1
            else:
                if y_dist < 0:
                    tt[1] -= 1
        else:
            if x_dist < -1:
                tt[0] -= 1
                if y_dist > 0:
                    tt[1] += 1
                else:
                    if y_dist < 0:
                        tt[1] -= 1

        if y_dist > 1:
            tt[1] += 1
            if x_dist > 0:
                tt[0] += 1
            else:
                if x_dist < 0:
                    tt[0] -= 1
        else:
            if y_dist < -1:
                tt[1] -= 1
                if x_dist > 0:
                    tt[0] += 1
                else:
                    if x_dist < 0:
                        tt[0] -= 1
        return tt


for line in file_line:
    line = line.strip().split(' ')
    d = line[0]
    s = int(line[1])
    if d == 'D':
        for m in range(s):
            h[0] = h[0] - 1
            if not (is_t_touch(h, t)):
                if not (need_diag_move(h, t)):
                    t[0] = t[0] - 1
                else:
                    t = move_t_diag(h, t, d, m)
                visited.append(str(t))
            # show_board( h, t)
    if d == 'U':
        for m in range(s):
            h[0] = h[0] + 1
            if not (is_t_touch(h, t)):
                if not (need_diag_move(h, t)):
                    t[0] = t[0] + 1
                else:
                    t = move_t_diag(h, t, d, m)
                visited.append(str(t))
    if d == 'L':
        for m in range(s):
            h[1] = h[1] - 1
            if not (is_t_touch(h, t)):
                if not (need_diag_move(h, t)):
                    t[1] = t[1] - 1
                else:
                    t = move_t_diag(h, t, d, m)
                visited.append(str(t))
            # show_board( h, t)
    if d == "R":
        for m in range(s):
            h[1] = h[1] + 1
            if not (is_t_touch(h, t)):
                if not (need_diag_move(h, t)):
                    t[1] = t[1] + 1
                else:
                    t = move_t_diag(h, t, d, m)
                visited.append(str(t))
            # show_board(h, t)

print(len(set(visited)) + 1)
# 6098

print('part two')
h = [0, 0]
t = [0, 0]
visited = []
v = []
rope_knots = [
    [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]
]
for line in file_line:
    line = line.strip().split(' ')
    d = line[0]
    s = int(line[1])
    print(line)
    for m in range(s):
        for kn in range(len(rope_knots) - 1):
            h = rope_knots[kn]
            t = rope_knots[kn + 1]
            if d == 'D':
                if kn == 0:
                    h[0] = h[0] - 1
                if not (is_t_touch(h, t)):
                    if not (need_diag_move(h, t)):
                        t[0] = t[0] - 1
                    else:
                        t = move_t_diag(hh=h, tt=t, dd=d,mm=m )
            if d == 'U':
                if kn == 0:
                    h[0] = h[0] + 1
                if not (is_t_touch(h, t)):
                    if not (need_diag_move(h, t)):
                        t[0] = t[0] + 1
                    else:
                        t = move_t_diag(hh=h, tt=t, dd=d, mm=m)
            if d == 'L':
                if kn == 0:
                    h[1] = h[1] - 1
                if not (is_t_touch(h, t)):
                    if not (need_diag_move(h, t)):
                        t[1] = t[1] - 1
                    else:
                        t = move_t_diag(hh=h, tt=t, dd=d, mm=m)

            if d == "R":
                if kn == 0:
                    h[1] = h[1] + 1
                if not (is_t_touch(h, t)):
                    if not (need_diag_move(h, t)):
                        t[1] = t[1] + 1
                    else:
                        t = move_t_diag(hh=h, tt=t, dd=d, mm=m)

            rope_knots[kn] = h
            rope_knots[kn + 1] = t
            print(rope_knots)
            input('wait')

            visited.append(str(rope_knots[len(rope_knots) - 1]))

    print(rope_knots)
    input('wait')

print(visited)
print(set(visited))
print(len(set(visited)) + 1)
# 6099 too high
