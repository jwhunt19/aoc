import os
import re

script_dir = os.path.dirname(os.path.realpath(__file__))
# input_file_path = os.path.join(script_dir, "input.txt")
input_file_path = os.path.join(script_dir, "example.txt")

with open(input_file_path, encoding="utf-8") as input_file:
    input_file = input_file.read()


# shape raw file data
def shape_data(file):
    seed_list = get_seed_list(file)
    seed_maps = {}

    maps = file.split("\n\n")[1:]
    for seed_map in maps:
        source, destination, ranges = build_map_data(seed_map)
        seed_maps[source] = {"destination": destination, "ranges": ranges}

    return seed_list, seed_maps


# converts first line of file into readable seed list
def get_seed_list(file):
    seed_list = file.split("\n")[0]  # grab seed list from first line of the file
    seed_list = seed_list.split(":")  # split "seed" key from seed values
    seed_list = seed_list[1].split()  # set to array of seeds

    return seed_list


# shapes raw seed_map to it's revelvant parts
def build_map_data(seed_map):
    # splits map data into parts to be assigned (split on "-", " map", and \n)
    seed_map_data = re.split(r"[-]|\s+(?=map)|\n", seed_map)

    map_source = seed_map_data[0]  # set source for map
    map_dest = seed_map_data[2]  # set destination for map

    seed_ranges = seed_map_data[4:]  # assign rest of the data to ranges
    for i, _ in enumerate(seed_ranges):  # convert each line from a string to a list
        seed_ranges[i] = seed_ranges[i].split()

    return map_source, map_dest, seed_ranges


# gets path and location for each seed
def get_seed_paths(seed_list, maps):
    seed_paths_dict = {}

    for seed in seed_list:
        seed_path = []  # list of all destination numbers
        source = "seed"  # source to reference current map
        cur_num = int(seed)  # current source number for referencing map
        while source:  # while there is a valid next source
            seed_map = maps[source]


            # TODO: add logic here to look at difference of source/dest nums
            

            seed_path.append(cur_num)  # add destination num to list

            if maps.get(seed_map["destination"]):  # if the next destination exists
                source = seed_map[
                    "destination"
                ]  # continue to new destination if exists
            else:
                source = None  # end loop if not, location has been reached

        seed_paths_dict[seed] = {
            "path": seed_path,
            "location": seed_path[len(seed_path) - 1],
        }

    return seed_paths_dict


def get_lowest_location(paths):
    locations = []

    for _, path in paths.items():
        locations.append(path["location"])

    locations.sort()

    return locations[0]


seeds, seed_maps_dict = shape_data(input_file)

# print(lowest_location)

print("seeds: ", seeds)
print("seed_map_dict: ", seed_maps_dict)
