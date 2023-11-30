# A Rock
# B Paper
# C Scissors

# X Rock 1
# Y Paper 2
# Z Scissors 3

# 0 if lose
# 3 if draw
# 6 if won

file1 = open('day2_input.txt', 'r')
file_lines = file1.readlines()
score = 0

player0win = 'PaperRockScissorsPaper'
player1win = 'PaperScissorsRockPaper'

game_map = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X': "Rock", 'Y': 'Paper', 'Z': 'Scissors'}
shape_score = {'Rock': 1, 'Paper': 2, 'Scissors': 3}

# for line in file_lines:
#    play = line.strip().split(' ')
#    play[0] = game_map[play[0]]
#    play[1] = game_map[play[1]]
#
#    if play[0] == play[1]:  # draw
#        score = score + shape_score[play[1]] + 3
#    else:
#        if play[0] + play[1] in player0win:  # Lose add 0
#            score = score + shape_score[play[1]]
#        else:
#            score = score + shape_score[play[1]] + 6  # win
# print(score)


# part two

lose_map = {'Rock': 'Scissors', 'Paper': 'Rock', 'Scissors': 'Paper'}
win_map = {'Rock': 'Paper', 'Paper': 'Scissors', 'Scissors': 'Rock'}

# x = lose
# y = draw
# z = win

for line in file_lines:
    play = line.strip().split(' ')
    play[0] = game_map[play[0]]

    if play[1] == 'Y':  # draw
        score = score + shape_score[play[0]] + 3
    else:
        if play[1] == 'X':  # lose
            score = score + shape_score[lose_map[play[0]]]
        else:
            score = score + shape_score[win_map[play[0]]] + 6  # win
print(score)
# 14859
