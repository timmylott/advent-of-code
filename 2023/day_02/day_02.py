file1 = open('day_02_input.txt', 'r')
file_lines = file1.readlines()

red = 12
green = 13
blue = 14

game_red = True
game_green = True
game_blue = True

possible_game_total = 0
possible_game = []

for line in file_lines:
    game = line.strip().split(':')
    for game_set in game[1].split(';'):
        for cube in game_set.split(','):
            if cube.split(' ')[2].strip() == 'red':
                if int(cube.split(' ')[1]) > red:
                    game_red = False
            if cube.split(' ')[2].strip() == 'green':
                if int(cube.split(' ')[1]) > green:
                    game_green = False
            if cube.split(' ')[2].strip() == 'blue':
                if int(cube.split(' ')[1]) > blue:
                    game_blue = False

    if game_red and game_blue and game_green:
        possible_game_total = possible_game_total + int(game[0].split(' ')[1])
        possible_game.append(game[0])
    game_red = True
    game_green = True
    game_blue = True

print(possible_game_total)
print(possible_game)

# part two


possible_game_total = 0
possible_game = []

game_red_list = []
game_green_list = []
game_blue_list = []
total_game_power = 0

for line in file_lines:
    game = line.strip().split(':')
    for game_set in game[1].split(';'):
        for cube in game_set.split(','):
            if cube.split(' ')[2].strip() == 'red':
                if int(cube.split(' ')[1]) > red:
                    game_red = False
                game_red_list.append(int(cube.split(' ')[1]))
            if cube.split(' ')[2].strip() == 'green':
                if int(cube.split(' ')[1]) > green:
                    game_green = False
                game_green_list.append(int(cube.split(' ')[1]))
            if cube.split(' ')[2].strip() == 'blue':
                if int(cube.split(' ')[1]) > blue:
                    game_blue = False
                game_blue_list.append(int(cube.split(' ')[1]))
    game_power = max(game_red_list) * max(game_green_list) * max(game_blue_list)
    total_game_power = total_game_power + game_power

    if game_red and game_blue and game_green:
        possible_game_total = possible_game_total + int(game[0].split(' ')[1])
        possible_game.append(game[0])
    game_red = True
    game_green = True
    game_blue = True

    game_red_list = []
    game_green_list = []
    game_blue_list = []

print(possible_game_total)
print(possible_game)
print(total_game_power)

