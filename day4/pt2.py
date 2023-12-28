from input import input

# input = [
#     {"winning_nums": [41, 48, 83, 86, 17], "my_nums": [83, 86,  6, 31, 17,  9, 48, 53]},
# {"winning_nums": [13, 32, 20, 16, 61], "my_nums": [61, 30, 68, 82, 17, 32, 24, 19]},
# {"winning_nums": [ 1, 21, 53, 59, 44], "my_nums": [69, 82, 63, 72, 16, 21, 14,  1]},
# {"winning_nums": [41, 92, 73, 84, 69], "my_nums": [59, 84, 76, 51, 58,  5, 54, 83]},
# {"winning_nums": [87, 83, 26, 28, 32], "my_nums": [88, 30, 70, 12, 93, 22, 82, 36]},
# {"winning_nums": [31, 18, 13, 56, 72], "my_nums": [74, 77, 10, 23, 35, 67, 36, 11]},
# ]

num_of_cards = 0
card_dict = {}
for i in range(len(input)):
    card_dict[i+1] = 1

card_number = 1
for card in input:
    wins = 0
    for num in card["my_nums"]:
        if num in card["winning_nums"]:
            wins += 1
    for i in range(card_dict[card_number]):
        for j in range(wins):
            card_dict[card_number + 1 + j] += 1
    wins = 0
    num_of_cards += card_dict[card_number]
    card_number += 1
print(num_of_cards)
