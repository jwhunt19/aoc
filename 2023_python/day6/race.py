import os
import functools


# parse file data
def parse_data(data, day):
    times = []
    distances = []
    for i, data in enumerate(file.readlines()):
        data = data.split(":")[1].split()

        # optional flag check for day 2
        if day == 2:
            # concat nums into one num, list for compatibility with previous code
            data = ["".join(data)]

        data = [int(n) for n in data]

        if i == 0:
            times = data
        else:
            distances = data

    return times, distances


# get win count
def get_win_count(times, distances):
    win_num_list = []

    for i, _ in enumerate(times):
        t = times[i]
        d = distances[i]
        outcomes = []

        for i in range(t):
            # equation for getting race distance
            outcomes.append(i * (t - i))

        # filter out wins if greater than distance
        wins = list(filter(lambda n: n > d, outcomes))
        win_num_list.append(len(wins))

    return win_num_list


# reduce wins to product
def get_wins_product(wins):
    return functools.reduce(lambda a, c: a * c, wins)


# file path
script_dir = os.path.dirname(os.path.realpath(__file__))
input_file_path = os.path.join(script_dir, "input.txt")

with open(input_file_path, encoding="utf-8") as file:
    DAY = 2
    times_list, distances_list = parse_data(file, DAY)

win_list = get_win_count(times_list, distances_list)
wins_product = get_wins_product(win_list)

print(wins_product)
