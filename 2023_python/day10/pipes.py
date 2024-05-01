N = "N"
E = "E"
S = "S"
W = "W"


def parse_data(data):
    maze = []
    start = None
    row = 0

    for line in data:
        line = line.strip()
        line = list(line)
        maze.append(line)

        if start:
            continue

        # get starting cords
        col = 0
        for char in line:
            if char == "S":
                start = [row, col]
            col += 1

        row += 1

    return maze, start


def get_furthest_distance(maze, start):
    steps = 0
    cur_pipe = "S"
    cords = start
    prev_dir = None

    while cur_pipe != "S" or steps == 0:

        for direction in pipe_directions[cur_pipe]:

            if prev_dir == direction:
                continue

            # get cords of next cell
            x, y = traverse(direction, cords)
            cell = maze[x][y]
            if cell == ".":
                continue

            # check if the next cell has a connecting pipe
            connecting_dir = pipe_match[direction]
            if connecting_dir not in pipe_directions[cell]:
                continue

            prev_dir = connecting_dir
            cur_pipe = cell
            cords = [x, y]
            break

        steps += 1

    return int(steps / 2)


def traverse(direction, cords):
    new_cords = cords.copy()

    if direction == N:
        new_cords[0] -= 1
        return new_cords
    elif direction == E:
        new_cords[1] += 1
        return new_cords
    elif direction == S:
        new_cords[0] += 1
        return new_cords
    elif direction == W:
        new_cords[1] -= 1
        return new_cords
    else:
        return cords


pipe_directions = {
    "S": {N, E, S, W},
    "|": {N, S},
    "-": {E, W},
    "L": {N, E},
    "J": {N, W},
    "7": {S, W},
    "F": {E, S},
}

pipe_match = {
    N: S,
    E: W,
    S: N,
    W: E,
}


with open("2023_python/day10/example.txt", encoding="utf-8") as file:
    lines = file.readlines()
    pipes_maze, start_cords = parse_data(lines)

DISTANCE = get_furthest_distance(pipes_maze, start_cords)

print(DISTANCE)
