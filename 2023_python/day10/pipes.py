# cardinal direction constants
N = "N"
E = "E"
S = "S"
W = "W"


# parse data for maze and starting point cords
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


# traverse the maze and returns the furthest distance and cords of the shape
def travel_maze_loop(maze, start):
    steps = 0
    cur_pipe = "S"
    cords = start
    prev_dir = None
    shape = []

    while cur_pipe != "S" or steps == 0:
        shape.append(cords.copy())

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

    return int(steps / 2), shape


# return next cell in given direction
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


# for getting area of maze with coordinates of its vertices
def shoelace_formula(shape):
    x_sum = 0
    y_sum = 0

    for i, cord in enumerate(shape):
        x1, y1 = cord
        x2, y2 = None, None
        if i == len(shape) - 1:
            x2, y2 = shape[0]
        else:
            x2, y2 = shape[i + 1]

        x_sum += x1 * y2
        y_sum += y1 * x2

    return abs((x_sum - y_sum) / 2)


# get points in maze using area and boundary length
def picks_theorem(area, boundary):
    return area - boundary / 2 + 1


# compatible directions for each pipe
pipe_directions = {
    "S": {N, E, S, W},
    "|": {N, S},
    "-": {E, W},
    "L": {N, E},
    "J": {N, W},
    "7": {S, W},
    "F": {E, S},
}

# match connecting pipe directions
pipe_match = {
    N: S,
    E: W,
    S: N,
    W: E,
}

# open input file
with open("2023_python/day10/input.txt", encoding="utf-8") as file:
    lines = file.readlines()
    pipes_maze, start_cords = parse_data(lines)

# get furthest distance and shape of maze loop
DISTANCE, SHAPE = travel_maze_loop(pipes_maze, start_cords)

# get area and amount of inner points of maze loop
AREA = shoelace_formula(SHAPE)
INNER_POINTS = picks_theorem(AREA, len(SHAPE))

print(INNER_POINTS)
print(DISTANCE)
