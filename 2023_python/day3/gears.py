gears_matrix = open("2023_python/day3/input.txt").read().splitlines()  # real input
# gears_matrix = open("2023_python/day3/example.txt").read().splitlines()  # example input


def check_row_for_valid_nums(row, row_index, matrix, valid_nums, gears):
    cur_num = ""  # current number for loop
    row_range = []  # indices to check around number on row
    # filter out indices outside of matrix range (below 0, above matrix length)
    col_range = list(
        filter(
            lambda i: i > -1 and i < len(matrix),
            [row_index - 1, row_index, row_index + 1],
        )
    )
    valid_flag = False

    # iterate over characters in row, build and add cur_num if valid
    for i, char in enumerate(row):
        if char.isnumeric():
            cur_num += char
            row_range.append(i)
        if not char.isnumeric() or i == len(row) - 1:
            if len(cur_num) != 0:
                # add row check left or right, if valid row index
                if row_range[0] > 0:
                    row_range.insert(0, row_range[0] - 1)
                if row_range[len(row_range) - 1] < len(row) - 1:
                    row_range.append(row_range[len(row_range) - 1] + 1)

                # check all surrounding values in matrix
                for col_i in col_range:
                    for row_i in row_range:
                        cell = matrix[col_i][row_i]  # current cell
                        coords = f"{col_i}.{row_i}"  # col/row position of current cell

                        if not cell.isalnum() and cell != ".":
                            valid_flag = True
                            # if current cell is a gear (*) add num to dictionary
                            if cell == "*":
                                if not gears.get(coords):
                                    gears[coords] = []
                                    gears[coords].append(cur_num)
                                else:
                                    gears[coords].append(cur_num)

                # if special character is adjacent, add to valid_nums
                if valid_flag:
                    valid_nums.append(int(cur_num))

                # reset after adding current number
                cur_num = ""
                row_range = []
                valid_flag = False

    return valid_nums


def check_matrix(matrix):
    valid_nums = []  # Initialize valid_nums as an empty list
    gears = {}

    # check each row for valid numbers
    for i, row in enumerate(matrix):
        valid_nums = check_row_for_valid_nums(row, i, matrix, valid_nums, gears)

    return valid_nums, gears


# get gear ratios by multiplying nums adjacent to gear when there are exactly 2
def get_gear_ratios(gears):
    gear_ratios = []

    for _, nums in gears.items():
        if len(nums) == 2:
            gear_ratios.append(int(nums[0]) * int(nums[1]))

    return gear_ratios


all_valid_nums, gears_dict = check_matrix(gears_matrix)  # get all valid nums
gears_sum = sum(all_valid_nums)  # sum all valid nums

gear_ratios_arr = get_gear_ratios(gears_dict)  # get gear ratios
gear_ratios_sum = sum(gear_ratios_arr)  # sum gear ratios

print(gear_ratios_sum)
print(gears_sum)
