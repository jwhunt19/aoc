import re

input = open("2023_python/day1/input.txt", "r").read()
calibrationValues = re.split("\s", input)

total = 0

for val in calibrationValues:
    min = 0
    max = 0
    for char in val:
        if char.isnumeric() and min == 0:
            min = char
            max = char
        elif char.isnumeric():
            max = char
    total += int(min+max)

print(total)

# continue with part 2 - https://adventofcode.com/2023/day/1#part2