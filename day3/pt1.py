from input import input


num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbol_list = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "<", ">", "/", "-", "+", "="]
symbol_dict = {}
result = 0

input_list = input.splitlines()

# builds symbol location dictionary
# keys are the number list, and the value is a list of number locations
for x in range(len(input_list)):
    line = input_list[x]
    symbol_dict[x] = []
    for i in range(len(line)):
        if line[i] in symbol_list:
            symbol_dict[x].append(i)

for y in range(len(input_list)):
    line = list(input_list[y])
    for z in range(len(line)-1):
        part_number_check = False
        part_number = None
        if line[z] in num_list:
            if z > 0:
                # left: line[z-1]
                if line[z-1] in symbol_list:
                    part_number_check = True
                    part_number = line[z]
            if z < len(line) - 1:
                # right: line[z+1]
                if line[z+1] in symbol_list:
                    part_number_check = True
                    part_number = line[z]
            if y > 0:
                # above: input_list[y-1][z]
                if input_list[y-1][z] in symbol_list:
                    part_number_check = True
                    part_number = line[z]
                if z > 0:
                    # above-left: input_list[y-1][z-1]
                    if input_list[y-1][z-1] in symbol_list:
                        part_number_check = True
                        part_number = line[z]

                if z < len(line):
                    # above-right: input_list[y-1][z+1]
                    if input_list[y-1][z+1] in symbol_list:
                        part_number_check = True
                        part_number = line[z]

            if y < len(input_list) - 1:
                # bottom: input[y+1][z]
                if input_list[y+1][z] in symbol_list:
                    part_number_check = True
                    part_number = line[z]
                if z > 0:
                    # bottom-left: input[y+1][z-1]
                    if input_list[y+1][z-1] in symbol_list:
                        part_number_check = True
                        part_number = line[z]
                if z < len(line):
                    # bottom-right: input[y+1][z+1]
                    if input_list[y+1][z+1] in symbol_list:
                        part_number_check = True
                        part_number = line[z]

        if part_number_check == True:
            for num in range(z + 1, len(line)):
                if line[num] in num_list:
                    part_number += line[num]
                    line[num] = "."
                else:
                    break
            for num in range(z-1, -1, -1):
                if line[num] in num_list:
                    part_number = line[num] + part_number
                    line[num] = "."
                else:
                    break
        if part_number != None:
            result += int(part_number)

print("\n\n\n result:", result)
