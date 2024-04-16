gears_matrix = open("2023_python/day3/input.txt").read().splitlines()  # real input
# gears_matrix = open("2023_python/day3/example.txt").read().splitlines()  # example input


def check_row_for_valid_nums(row, row_index, matrix, valid_nums):
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

                        if (
                            not matrix[col_i][row_i].isalnum()
                            and matrix[col_i][row_i] != "."
                        ):
                            valid_flag = True

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

    # check each row for valid numbers
    for i, row in enumerate(matrix):
        valid_nums = check_row_for_valid_nums(row, i, matrix, valid_nums)

    return valid_nums


all_valid_nums = check_matrix(gears_matrix)  # get all valid nums
gears_sum = sum(all_valid_nums)  # sum all valid nums

print(gears_sum)
