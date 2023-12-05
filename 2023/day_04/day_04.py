import re

file1 = open('day_04_input.txt', 'r')
file_lines = file1.readlines()

card_points = 0
total_points = 0

for line in file_lines:
    line = line.strip().split(':')[1].strip()
    winning_numbers = line.split('|')[0].strip().split(' ')
    my_numbers = line.split('|')[1].strip().split(' ')
    for nbr in my_numbers:
        if nbr != '':
            if nbr in winning_numbers:
                if card_points == 0:
                    card_points = 1
                else:
                    card_points = card_points + card_points
    total_points = total_points + card_points
    card_points = 0

print(total_points)


# part 2

file1 = open('day_04_input.txt', 'r')
file_lines = file1.readlines()

card_wins = 0
total_cards = 0
card_wins_list = {}

new_stack = {}

for line in file_lines:
    card = line.strip().split(':')[0].strip()
    line = line.strip().split(':')[1].strip()
    winning_numbers = line.split('|')[0].strip().split(' ')
    my_numbers = line.split('|')[1].strip().split(' ')
    for nbr in my_numbers:
        if nbr != '':
            if nbr in winning_numbers:
                card_wins = card_wins + 1
    card_wins_list[re.sub(r'\s+', ' ', card).split(' ')[1]] = card_wins
    card_wins = 0

for card, wins in card_wins_list.items():
    new_stack[card] = 1

for card in new_stack:
    for i in range(new_stack[card]):
        current_wins = card_wins_list[card]
        for x in range(1, current_wins + 1):
            new_stack[str(int(card) + x)] = new_stack[str(int(card) + x)] + 1

print(new_stack)
print(sum(new_stack.values()))
