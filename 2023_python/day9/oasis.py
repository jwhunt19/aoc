def next_value(history):
    value = 0
    vals = history
    next_vals = []
    all_zeroes = False
    while not all_zeroes:
        for i, n in enumerate(vals):
            if i != 0:
                next_vals.append(n - vals[i - 1])

            if i == len(vals) - 1:
                value += n
                all_zeroes = all([x == 0 for x in next_vals])
                vals = next_vals
                next_vals = []

    return value


next_value_sums = 0

with open("2023_python/day9/input.txt", encoding="utf-8") as file:
    for line in file.readlines():
        history_nums = [int(n) for n in line.split()]
        next_value_sums += next_value(history_nums)

print(next_value_sums)