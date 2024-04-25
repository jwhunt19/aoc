import os


def parse_data(data):
    dirs = ""
    paths_map = {}

    dirs_done = False
    for line in data.readlines():
        if line == "\n":
            dirs_done = True
            continue

        if not dirs_done:
            dirs += line.strip()
        else:
            map_node, paths = line.split("=")

            map_node = map_node.strip()

            paths = paths.split(",")
            for i, p in enumerate(paths):
                paths[i] = p.strip("( )\n")
            paths = {L: paths[0], R: paths[1]}

            paths_map[map_node] = paths

    return dirs, paths_map


def walk_path(dirs, paths):
    steps = 0
    pos = "AAA"

    while pos != "ZZZ":
        for d in dirs:
            steps += 1
            pos = paths[pos][d]

    return steps


L = "L"
R = "R"

# file path
script_dir = os.path.dirname(os.path.realpath(__file__))
input_file_path = os.path.join(script_dir, "input.txt")

# open file and parse file
with open(input_file_path, encoding="utf-8") as file:
    directions, paths_dict = parse_data(file)


STEPS_TAKEN = walk_path(directions, paths_dict)
print(STEPS_TAKEN)
