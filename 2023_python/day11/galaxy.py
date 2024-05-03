def expand_universe(galaxies_map):
    empty_rows = get_empty_rows(galaxies_map)
    empty_cols = get_empty_cols(galaxies_map)

    new_map = []

    for i, row in enumerate(galaxies_map):
        adjustment = 0
        for col in empty_cols:
            row.insert(col + adjustment, ".")
            adjustment += 1

        new_map.append(row)

        if i in empty_rows:
            new_map.append(row)

    return new_map


def get_empty_rows(galaxies_map):
    return [i for i, row in enumerate(galaxies_map) if "#" not in row]


def get_empty_cols(galaxies_map):
    empty_cols = []

    for i in range(len(galaxies_map[0]) - 1):
        if any([row[i] == "#" for row in galaxies_map]):
            continue
        empty_cols.append(i)

    return empty_cols


def get_galaxy_cords(galaxies_map):
    galaxy_cords = set()

    for i, row in enumerate(galaxies_map):
        for j, cell in enumerate(row):
            if cell == "#":
                galaxy_cords.add((i, j))

    return galaxy_cords


def sum_of_all_paths(galaxy_cords):
    distances_sum = 0
    checked = {}

    for i, cords in enumerate(galaxy_cords):
        for j, compare_cords in enumerate(galaxy_cords):

            if i == j:
                continue

            if compare_cords in checked.get(cords, []):
                continue

            distance = abs(
                abs(cords[0] - compare_cords[0]) + abs(cords[1] - compare_cords[1])
            )

            checked[compare_cords] = checked.get(compare_cords, []) + [cords]
            distances_sum += distance

    return distances_sum


with open("2023_python/day11/input.txt", encoding="utf-8") as file:
    galaxy_map_raw = []
    for line in file.readlines():
        line = line.strip()
        line = list(line)
        galaxy_map_raw.append(line)


galaxies_map_expanded = expand_universe(galaxy_map_raw)
galaxy_coordinates = get_galaxy_cords(galaxies_map_expanded)
sum_of_paths = sum_of_all_paths(galaxy_coordinates)

print("sum: ", sum_of_paths)
# print("galaxy_coordinates: ", galaxy_coordinates)

# print("galaxy map: ")
# for r in galaxies_map_expanded:
#     print(r)
