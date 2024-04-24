import os
import functools
import time # TODO: delete

start_time = time.time()  # Get the current time in seconds

# parse file data
def parse_data(data, day):
    times = []
    distances = []
    for i, data in enumerate(file.readlines()):
        data = data.split(":")[1].split()
        if day == 2:
            data = ["".join(data)]
        data = [int(n) for n in data]
        
            

        if i == 0:
            times = data
        else:
            distances = data

    return times, distances


# get times
def get_win_counts(times, distances):
    win_num_list = []

    for i, _ in enumerate(times):
        t = times[i]
        d = distances[i]
        win_nums = 0

        for i in range(t):
            cur_dist = 0
            cur_time = 0
            speed = 0
            hold = True

            while cur_time < t:
                if cur_time >= i:
                    hold = False
                if hold:
                    speed += 1
                else:
                    cur_dist += speed

                cur_time += 1

            if cur_dist > d:
                win_nums += 1

        win_num_list.append(win_nums)

    return win_num_list


def get_wins_product(wins):
    return functools.reduce(lambda a, c: a * c, wins)


# file path
script_dir = os.path.dirname(os.path.realpath(__file__))
input_file_path = os.path.join(script_dir, "example.txt")

with open(input_file_path, encoding="utf-8") as file:
    DAY = 1
    times_list, distances_list = parse_data(file, DAY)

win_list = get_win_counts(times_list, distances_list)
wins_product = get_wins_product(win_list)

print(wins_product)

end_time = time.time()  # Get the current time again
# time taken in MM:SS:MS
print("Time taken: ", time.strftime("%M:%S:%MS", time.gmtime(end_time - start_time)))  # TODO: delete
