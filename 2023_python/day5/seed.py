import os

script_dir = os.path.dirname(os.path.realpath(__file__))
# input_file_path = os.path.join(script_dir, "input.txt")
input_file_path = os.path.join(script_dir, "example.txt")

print(input_file_path)

with open(input_file_path, encoding="utf-8") as input_file:
    input_file = input_file.read()


def shape_data(file):
    file = file.split("\n\n")
    seed_data = None
    seed_maps_dict = {}

    for f in file:
        m = f.split(":")  # split map id from ranges
        m[0] = m[0].split()[0]  # remove map from end of key word

        if m[0] == "seeds":  # strip white space from seeds, assign to seeds var
            m[1] = m[1].strip()
            m[1] = m[1].split()
            seed_data = m[1]
        else:  # split seed map lines, remove first empty line, assign to dict
            m[1] = m[1].split("\n")
            m[1].pop(0)
            seed_maps_dict[m[0]] = m[1]

    return seed_data, seed_maps_dict


seeds, seed_map_dict = shape_data(input_file)

print(seeds)
print(seed_map_dict)
