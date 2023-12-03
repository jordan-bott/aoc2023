from input import input

result = 0
red_list = ["red", "red,"]
blue_list = ["blue", "blue,"]
green_list = ["green", "green,"]

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
            elif item in green_list and int(turn_list[c-1]) > 13:
                # print("\ngreen fail")
                green = False
                break
            elif item in blue_list and int(turn_list[c-1]) > 14:
                # print("\nblue fail")
                blue = False
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
