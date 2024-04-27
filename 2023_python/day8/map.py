import os


def parse_data(data):
    dirs = ""
    paths_map = {}
    ghost_starts_list = []

    dirs_done = False
    for line in data.readlines():
        if line == "\n":
            dirs_done = True
            dirs = list(dirs)
            continue

        if not dirs_done:
            dirs += line.strip()
        else:
            map_node, paths = line.split("=")

            map_node = map_node.strip()

            if GHOST_MODE:
                if map_node.endswith("A"):
                    ghost_starts_list.append(map_node)

            paths = paths.split(",")
            for i, p in enumerate(paths):
                paths[i] = p.strip("( )\n")
            paths = {L: paths[0], R: paths[1]}

            paths_map[map_node] = paths

    return dirs, paths_map, ghost_starts_list


def ghost_walk(dirs, paths, starts):
    steps = []
    for start in starts:
        s = walk_path(dirs, paths, start)
        steps.append(s)

    return steps


def walk_path(dirs, paths, pos="AAA"):
    steps = 0

    dirs_queue = dirs.copy()
    dirs_queue.reverse()
    dirs_refresh = dirs_queue.copy()

    while not pos.endswith("Z"):
        if not dirs_queue:
            dirs_queue = dirs_refresh.copy()

        steps += 1
        pos = paths[pos][dirs_queue.pop()]

    return steps


def lowest_common_multiple(nums):
    l = nums.pop()
    while nums:
        l = lcm(l, nums.pop())

    return l


def gdc(a, b):
    c = a % b
    if c == 0:
        return b
    else:
        return gdc(b, c)


def lcm(a, b):
    return a * b / gdc(a, b)


L = "L"
R = "R"

# file path
script_dir = os.path.dirname(os.path.realpath(__file__))
input_file_path = os.path.join(script_dir, "input.txt")

# flag for ghost mode (day 2)
GHOST_MODE = True

# open file and parse file
with open(input_file_path, encoding="utf-8") as file:
    directions, paths_dict, ghost_starts = parse_data(file)

if GHOST_MODE:
    STEPS_TAKEN = ghost_walk(directions, paths_dict, ghost_starts)
else:
    STEPS_TAKEN = walk_path(directions, paths_dict)

STEPS_TAKEN = lowest_common_multiple(STEPS_TAKEN)

print(STEPS_TAKEN)
