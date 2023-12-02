# from input import input

result = 0
red_list = ["red", "red,"]
blue_list = ["blue", "blue,"]
green_list = ["green", "green,"]

input = {
    "1": "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "2": "1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "3": "8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "4": "1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "5": "6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
}

for game in input:
    game_list = input[game].split(";")
    red = True
    green = True
    blue = True
    for turn in game_list:
        turn_list = turn.split()
        # print(turn_list)
        for c in range(1, len(turn_list), 2):
            item = turn_list[c]
            # print(item, turn_list[c-1])
            if item in red_list and int(turn_list[c-1]) > 12:
                # print("\nred fail")
                red = False
                break
            elif item in blue_list and int(turn_list[c-1]) > 13:
                # print("\nblue fail")
                blue = False
                break
            elif item in green_list and int(turn_list[c-1]) > 14:
                # print("\ngreen fail")
                green = False
                break
        if red == False or blue == False or green == False:
            break
    # print("\n\n---------------", game)
    if red == True and blue == True and green == True:
        # print("++++++++++++++++++++++++")
        print(game, "            ", game_list)
        result += int(game)
    # print(result)


print(result)
