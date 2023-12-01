from day1_input import input

nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
nums_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}
sum = 0

for line in input.splitlines():
    temp_num = ""
    index_one = 0
    for x in range(0, len(line)):
        if line[x] in nums:
            temp_num += line[x]
            index_one = x
            break
        elif line[x:x+3] in nums_dict:
            temp_num += nums_dict[line[x:x+3]]
            index_one = x + 3
            break
        elif line[x:x+4] in nums_dict:
            temp_num += nums_dict[line[x:x+4]]
            index_one = x + 4
            break
        elif line[x:x+5] in nums_dict:
            temp_num += nums_dict[line[x:x+5]]
            index_one = x + 5
            break
    for y in range(len(line)-1, index_one-1, -1):
        if line[y] in nums:
            temp_num += line[y]
            break
        elif line[y:y+3] in nums_dict:
            temp_num += nums_dict[line[y:y+3]]
            index_one = y + 3
            break
        elif line[y:y+4] in nums_dict:
            temp_num += nums_dict[line[y:y+4]]
            index_one = y + 4
            break
        elif line[y:y+5] in nums_dict:
            temp_num += nums_dict[line[y:y+5]]
            index_one = y + 5
            break
    if temp_num != "":
        sum += int(temp_num)

print(sum)
