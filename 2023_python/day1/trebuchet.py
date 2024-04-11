import re

aoc_input = open("2023_python/day1/input.txt", "r").read()
calibration_values = re.split("\s", aoc_input)

alpha_nums = {
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

# replaces alpha nums w/ num format - "one" -> "1"
def get_alpha_nums(val_str):
    new_str = ""

    i = 0
    while i < len(val_str):
        if val_str[i].isalpha():
            test_input = val_str[i]
            j = i+1
            while j < len(val_str):
                if val_str[j].isalpha():
                    test_input += val_str[j]
                    if alpha_nums.get(test_input, None):
                        new_str += alpha_nums[test_input]
                    j += 1
                else:
                    break
        else:
            new_str += val_str[i]

        i += 1

    return new_str

# concat first and last number in each line, build sum total
def get_total_value(cv):
    total = 0

    for val in cv:
        numeric_val = get_alpha_nums(val)
        min = 0
        max = 0

        for char in numeric_val:
            if char.isnumeric() and min == 0:
                min = char
                max = char
            elif char.isnumeric():
                max = char

        total += int(min+max)

    return total


tv = get_total_value(calibration_values)
print("total:", tv)
