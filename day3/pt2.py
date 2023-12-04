from input import input


num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbol_list = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "<", ">", "/", "-", "+", "="]
symbol_dict = {}

input_list = input.splitlines()


for line in input_list:
    for item in line:
        if item not in symbol_list and item not in num_list and item != ".":
            print(item)
