from input import input


num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

input_list = input.splitlines()


for y in range(len(input_list)):
    line = list(input_list[y])
    gears = []
    gear_check = False
    for z in range(len(line)-1):
        if line[z] == "*":
            if z > 0:
                # left: line[z-1]
                if line[z-1] in num_list:
                    gears.append(z)
                    gear_check = True
            if z < len(line) - 1:
                # right: line[z+1]
                if line[z+1] in num_list:
                    gears.append(z)
                    gear_check = True
            if y > 0:
                # above: input_list[y-1][z]
                if input_list[y-1][z] in num_list:
                    gears.append(z)
                    gear_check = True
                if z > 0:
                    # above-left: input_list[y-1][z-1]
                    if input_list[y-1][z-1] in num_list:
                        gears.append(z)
                        gear_check = True

                if z < len(line):
                    # above-right: input_list[y-1][z+1]
                    if input_list[y-1][z+1] in num_list:
                        gears.append(z)
                        gear_check = True

            if y < len(input_list) - 1:
                # bottom: input[y+1][z]
                if input_list[y+1][z] in num_list:
                    gears.append(z)
                    gear_check = True
                if z > 0:
                    # bottom-left: input[y+1][z-1]
                    if input_list[y+1][z-1] in num_list:
                        gears.append(z)
                        gear_check = True
                if z < len(line):
                    # bottom-right: input[y+1][z+1]
                    if input_list[y+1][z+1] in num_list:
                        gears.append(z)
                        gear_check = True

        if len(gears) >= 2:
            for gear in gears:
