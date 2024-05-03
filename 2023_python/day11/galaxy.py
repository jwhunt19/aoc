# imports
from typing import List, Set, Tuple


# return all rows that are empty space
def get_empty_rows(galaxies_map: List[List[str]]) -> List[int]:
    return [i for i, row in enumerate(galaxies_map) if "#" not in row]


# return all columns that are empty space
def get_empty_cols(galaxies_map: List[List[str]]) -> List[int]:
    empty_cols = []

    for i in range(len(galaxies_map[0]) - 1):
        if any([row[i] == "#" for row in galaxies_map]):
            continue
        empty_cols.append(i)

    return empty_cols


# get the coordinates for every galaxy in the galaxies map
def get_galaxy_coords(galaxies_map: List[List[str]]) -> Set[Tuple[int, int]]:
    galaxy_coords = set()

    for i, row in enumerate(galaxies_map):
        for j, cell in enumerate(row):
            if cell == "#":
                galaxy_coords.add((i, j))

    return galaxy_coords


# returns sum of all path distances
def sum_of_all_paths(
    galaxy_coords: Set[Tuple[int, int]], empty_rows: List[int], empty_cols: List[int]
) -> int:
    distances_sum = 0
    checked = {}

    for i, current_coords in enumerate(galaxy_coords):
        for j, target_coords in enumerate(galaxy_coords):

            if i == j:
                continue

            if target_coords in checked.get(current_coords, []):
                continue

            distance = calc_distance(
                current_coords, target_coords, empty_rows, empty_cols
            )

            checked[target_coords] = checked.get(target_coords, []) + [current_coords]
            distances_sum += distance

    return distances_sum


# distance from point a to b, accounting for empty space jumps
def calc_distance(
    coord_a: Tuple[int, int],
    coord_b: Tuple[int, int],
    empty_rows: List[int],
    empty_cols: List[int],
) -> int:
    x1, y1 = coord_a
    x2, y2 = coord_b

    warp_jump_distance = 0
    warp_jump_distance += warp_jump([x1, x2], empty_rows)
    warp_jump_distance += warp_jump([y1, y2], empty_cols)

    return (abs(x1 - x2) + abs(y1 - y2)) + warp_jump_distance


# check every empty space crossed when jumping from position a to b
def warp_jump(positions: List[int], empty_spaces: List[int]) -> int:
    positions.sort()
    space_crossed = 0
    space_distance = 999999

    for empty_space in empty_spaces:
        if positions[0] < empty_space < positions[1]:
            space_crossed += 1

    return space_crossed * space_distance


# read and parse file
with open("2023_python/day11/input.txt", encoding="utf-8") as file:
    galaxies = []
    for line in file.readlines():
        line = line.strip()
        line = list(line)
        galaxies.append(line)

# get galaxy coords
galaxy_coordinates = get_galaxy_coords(galaxies)

# get empty space
empty_rows_list = get_empty_rows(galaxies)
empty_cols_list = get_empty_cols(galaxies)

# return sum of all paths
sum_of_paths = sum_of_all_paths(galaxy_coordinates, empty_rows_list, empty_cols_list)

print("sum: ", sum_of_paths)
