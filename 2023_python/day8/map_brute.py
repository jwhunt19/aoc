import os
import time

start_time = time.time()


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


def ghost_walk(dirs, paths, starts, s_map, z_steps=None, min_steps=None, ri=1):
    if not z_steps:
        z_steps = {}

    all_zs = []

    for start in starts:
        if not z_steps.get(start):
            pos = start
            z_steps[start] = {"pos": pos, "zs": set(), "steps": 0}
        else:
            pos = z_steps[start]["pos"]

        i = 0
        while i < 1500000:
            s, pos = walk_path(dirs, paths, pos, s_map)
            z_steps[start]["zs"].add(z_steps[start]["steps"] + s)
            z_steps[start]["steps"] += s
            i += 1

        if min_steps:
            z_steps[start]["zs"] = {
                z for z in z_steps[start]["zs"] if z % min_steps == 0
            }

        all_zs.append(z_steps[start]["zs"])

    if not min_steps:
        min_steps = min(sm["steps"] for sm in s_map.values())

    print_progress(ri * i, 1280372039, ri)

    matches = set.intersection(*all_zs)

    if matches:
        return min(matches)
    else:
        return ghost_walk(dirs, paths, starts, s_map, z_steps, min_steps, ri + 1)


def print_progress(prog, goal, ri):
    e_t = time.time()

    print("---------------------------")
    print(f"| recursion depth: {ri}/1000 |")
    print("------------------------------------------")
    print(f"| progress: {prog} / {goal} - {'{:.2f}%'.format(prog / goal * 100)}")
    print(time.strftime("| elapsed time - %H:%M:%S", time.gmtime(e_t - start_time)))
    print("------------------------------------------")
    print("|")


def walk_path(dirs, paths, pos="AAA", s_map=None):
    if s_map and s_map.get(pos):
        return s_map[pos]["steps"], s_map[pos]["pos"]
    else:
        steps = 0
        old_pos = pos
        s_map[pos] = {}

        dirs_queue = dirs.copy()
        dirs_queue.reverse()

        while steps == 0 or not pos.endswith("Z"):
            if not dirs_queue:
                dirs_queue = dirs.copy()
                dirs_queue.reverse()

            steps += 1
            pos = paths[pos][dirs_queue.pop()]

        s_map[old_pos] = {"steps": steps, "pos": pos}

        return steps, pos


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

step_map = {}

if GHOST_MODE:
    STEPS_TAKEN = ghost_walk(directions, paths_dict, ghost_starts, step_map)
else:
    STEPS_TAKEN = walk_path(directions, paths_dict)

print(STEPS_TAKEN)
