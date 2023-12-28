from input import input

points = 0
nums_won = 0
for card in input:
    for num in card["my_nums"]:
        if num in card["winning_nums"]:
            if nums_won == 0:
                nums_won += 1
            else:
                nums_won *= 2
        else:
            pass
    points += nums_won
    nums_won = 0

print(points)
