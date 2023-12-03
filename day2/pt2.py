from input import input

result = 0
red_list = ["red", "red,"]
blue_list = ["blue", "blue,"]
green_list = ["green", "green,"]

for game in input:
    game_list = input[game].split(";")
    red = 0
    green = 0
    blue = 0
    for turn in game_list:
        turn_list = turn.split()
        for c in range(1, len(turn_list), 2):
            item = turn_list[c]
            if item in red_list and int(turn_list[c-1]) > red:
                red = int(turn_list[c-1])
            elif item in green_list and int(turn_list[c-1]) > green:
                green = int(turn_list[c-1])
            elif item in blue_list and int(turn_list[c-1]) > blue:
                blue = int(turn_list[c-1])
    power = red * blue * green
    result += power


print(result)
