from day1_input import input

nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
sum = 0

for line in input.splitlines():
    temp_num = ""
    index_one = 0
    for x in range(0, len(line)):

        if line[x] in nums:
            temp_num += line[x]
            index_one = x
            break
    for y in range(len(line)-1, index_one-1, -1):
        if line[y] in nums:
            temp_num += line[y]
            break
    if temp_num != "":
        sum += int(temp_num)

print(sum)
