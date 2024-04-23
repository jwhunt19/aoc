import os


# parse data from file for seeds and map data
def parse_data(data):
    seeds = None
    maps = []
    cur_map = []

    for i, line in enumerate(data):
        if i == 0:
            seeds = parse_seeds(line)
        else:
            # if line is nums, split to list, convert to ints
            if line[0].isnumeric():
                map_line = line.split()
                map_line = list(map(int, map_line))
                cur_map.append(map_line)
            # else if line is blank, add current map and reset
            elif not line.strip() and len(cur_map) > 0:
                maps.append(cur_map)
                cur_map = []

    # add last map
    if cur_map:
        maps.append(cur_map)

    return seeds, maps


# parse seeds, convert to ints
def parse_seeds(line):
    seeds = line.split(":")[1].split()
    seeds = list(map(int, seeds))

    return seeds


# get seed ranges for each set of seed nums
def get_seed_ranges(seeds):
    ranges = []

    for i, _ in enumerate(seeds):
        if i % 2 == 0:
            seed_min = seeds[i]
            seed_max = seeds[i] + (seeds[i + 1] - 1)

            ranges.append([seed_min, seed_max])

    return ranges


# get list of locations associated with ranges
def get_locations(ranges, maps):
    for seed_map in maps:
        new_ranges = []
        for seed_range in ranges:
            segments = [seed_range]

            # iterate over each line of a map
            for line in seed_map:
                l_min = line[1]  # line min
                l_max = line[1] + (line[2] - 1)  # line max
                diff = line[0] - line[1]

                for i, segment in enumerate(segments):
                    s_min = segment[0]  # seed min
                    s_max = segment[1]  # seed max

                    # if entire seed range is in line range
                    if s_min >= l_min and s_max <= l_max:
                        segments = segments[0:i] + segments[i + 1 :]
                        new_ranges.append([s_min + diff, s_max + diff])

                    # if middle of seed range is in line range
                    if s_min <= l_min and s_max >= l_max:
                        segments = segments[0:i] + segments[i + 1 :]
                        segments.append([s_min, l_min - 1])
                        new_ranges.append([l_min + diff, l_max + diff])
                        segments.append([l_max + 1, s_max])

                    # if only end of seed range is in line range
                    if s_min < l_min and s_max >= l_min and s_max <= l_max:
                        segments = segments[0:i] + segments[i + 1 :]
                        segments.append([s_min, l_min - 1])
                        new_ranges.append([l_min + diff, s_max + diff])

                    # if only start of seed range is in line range
                    if s_min >= l_min and s_min <= l_max and s_max > l_max:
                        segments = segments[0:i] + segments[i + 1 :]
                        new_ranges.append([s_min + diff, l_max + diff])
                        segments.append([l_max + 1, s_max])

            if segments:
                new_ranges = new_ranges + segments

        ranges = new_ranges

    return ranges


def get_lowest(locations):
    flat_locations = [item for sublist in locations for item in sublist]

    lowest_number = min(flat_locations)

    return lowest_number


# file path
script_dir = os.path.dirname(os.path.realpath(__file__))
input_file_path = os.path.join(script_dir, "input.txt")

# read file
with open(input_file_path, encoding="utf-8") as seed_data:
    seed_list, map_list = parse_data(seed_data)

seed_ranges = get_seed_ranges(seed_list)

seed_locations = get_locations(seed_ranges, map_list)

lowest_location = get_lowest(seed_locations)

print(lowest_location)
