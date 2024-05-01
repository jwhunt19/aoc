# direction constants
N = "N"
E = "E"
S = "S"
W = "W"


def parse_data(data):
    maze = []

    start = None
    x = 0

    for row in data:
        row = row.strip()
        row = list(row)
        maze.append(row)

        # get starting cords
        if not start:
            y = 0
            for c in row:
                if c == "S":
                    start = [x, y]
                else:
                    y += 1
            x += 1

    return maze, start


def get_furthest_distance(maze, start):
    steps = 0

    pipe = "S"
    cords = start
    prev = None

    while pipe != "S" or steps == 0:
        if steps == 20000:
            break  # TODO DELETE

        # check current pipe possible directions
        for d in pipes_dict[pipe]:
            # don't check direction we came from
            if prev == d:
                continue
            # get cords of cell in provided direction
            x, y = traverse(d, cords)
            # ensure the cords are within the matrix
            if is_in_matrix(maze, [x, y]):
                cell = maze[x][y]
                if cell != ".":
                    connecting_dir = pipe_match[d]
                    if connecting_dir in pipes_dict[cell]:
                        pipe = cell
                        cords = [x, y]
                        prev = connecting_dir
                        break

        steps += 1

    return int(steps / 2)


def is_in_matrix(maze, cords):
    x_max = len(maze)
    y_max = len(maze[0])

    x = -1 < cords[0] < x_max
    y = -1 < cords[1] < y_max

    return x & y


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


pipes_dict = {
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


with open("2023_python/day10/input.txt", encoding="utf-8") as file:
    lines = file.readlines()
    pipes_maze, start_cords = parse_data(lines)

DISTANCE = get_furthest_distance(pipes_maze, start_cords)

print(DISTANCE)

# print(pipes_dict)
# print("----")
# print(pipes_maze)
# print("----")
# print(start_cords)
