def get_adjacent_values(history):
    next_value = 0
    prev_value = 0

    vals = history
    next_vals = []
    lowest_vals = []

    all_zeroes = False
    while not all_zeroes:
        for i, v in enumerate(vals):
            if i != 0:
                next_vals.append(v - vals[i - 1])
            else:
                lowest_vals.append(v)

            if i == len(vals) - 1:
                next_value += v
                all_zeroes = all([x == 0 for x in next_vals])
                vals = next_vals
                next_vals = []

    for i in range(len(lowest_vals) - 1, -1, -1):
        prev_value = lowest_vals[i] - prev_value

    return next_value, prev_value


NEXT_VALS_SUM = 0
PREV_VALS_SUM = 0

with open("2023_python/day9/input.txt", encoding="utf-8") as file:
    for line in file.readlines():
        history_nums = [int(n) for n in line.split()]
        next_v, prev_v = get_adjacent_values(history_nums)
        NEXT_VALS_SUM += next_v
        PREV_VALS_SUM += prev_v

print(NEXT_VALS_SUM, PREV_VALS_SUM)
