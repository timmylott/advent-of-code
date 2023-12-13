

def hand_type(card):
    card_count = {}
    for c in set(card):
        card_count[c] = card.count(c)

    card_values = []
    for lt in card:
        card_values.append(card_strength.index(lt))
    card_values.sort(reverse=True)
    if 5 in card_count.values():
        # five_of_a_kind
        return card, 9000, 'five_of_a_kind', card_values
    if 4 in card_count.values():
        # four_of_a_kind
        return card, 8000, 'four_of_a_kind', card_values
    if 3 in card_count.values() and 2 in card_count.values():
        # full_house'
        return card, 7000, 'full_house', card_values
    if 3 in card_count.values():
        # three_of_a_kind
        return card, 6000, 'three_of_a_kind', card_values
    if len({i for i in card_count if card_count[i]==2}) == 2:
        # two_pair
        return card, 5000, 'two_pair', card_values
    if 2 in card_count.values():
        # one_pair
        return card, 4000, 'one_pair', card_values

    #high_card
    return card, 3000, 'high_card', card_values

file1 = open('day_07_input.txt', 'r')
file_lines = file1.readlines()

card_strength = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
total_winnings = 0

new_stack = []
hand = {}
inserted = False
print(card_strength)
for line in file_lines:
    line = line.strip()
    hand['hand'], hand['type_num'], hand['type'], hand['card_values'] = hand_type(line.split(' ')[0])
    hand['bid'] = int(line.split(' ')[1])
    if len(new_stack) == 0:
        new_stack.append(hand.copy())
    else:
        for i in range(len(new_stack)):
            if new_stack[i]['type_num'] > hand['type_num']:
                new_stack.insert(i, hand.copy())
                inserted = True
                break;
            if new_stack[i]['type_num'] == hand['type_num']:
                new_stack_hand_values = new_stack[i]['card_values']
                hand_hand_values = hand['card_values']
                for cs in range(5):
                    # if new_stack_hand_values[cs] > hand_hand_values[cs] and not inserted:
                    #     if cs > 0:
                    #         new_stack.insert(i + 1, hand.copy())
                    #     else:
                    #         new_stack.insert(i, hand.copy())
                    #     inserted = True

                    if hand_hand_values[cs] > new_stack_hand_values[cs] and not inserted and i != len(new_stack)-1:
                        if i==0:
                            new_stack.insert(i+1, hand.copy())
                        else:
                            new_stack.insert(i, hand.copy())
                        inserted = True
                        break;
                    else:
                        if hand_hand_values[cs] != new_stack_hand_values[cs]:
                            if i == len(new_stack) - 1:
                                new_stack.insert(i, hand.copy())
                                inserted = True
                                break;
                            else:
                                new_stack.insert(i+1, hand.copy())
                                inserted = True
                                break;

                # if not inserted:
                #     if i==len(new_stack)-1:
                #         if hand_hand_values[cs] > new_stack_hand_values[cs]:
                #             new_stack.insert(i, hand.copy())
                #             inserted = True
                #         else:
                #             new_stack.append(hand.copy())
                #             inserted = True
                #     else:
                #         if cs == 4:
                #             new_stack.insert(i + 1, hand.copy())
                #             inserted = True
                #         else:
                #             new_stack.insert(i, hand.copy())
                #             inserted = True
            if inserted:
                break;
        if not inserted:
            new_stack.append(hand.copy())

        inserted = False

print(new_stack)

for i in range(len(new_stack)):
    total_winnings = total_winnings + (new_stack[i]['bid'] * (i+1))

print(total_winnings)

#974234365 to high
#884725804 to high
#884697817 to high
#889825736 not right
#245452104 not right
#245462608 not right
