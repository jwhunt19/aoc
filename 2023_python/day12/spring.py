from typing import List, Tuple, Dict


def parse_data(line: str) -> Tuple[str, List[int]]:
    springs, spring_counts = line.split()
    spring_counts = [int(x) for x in spring_counts.split(",")]
    spring_counts.reverse()

    return springs, spring_counts


def recurse_springs(
    springs: str,
    counts: List[int],
    i: int = 0,
    cur_group_count: int = 0,
    skip: bool = False,
) -> int:
    counts_copy = counts.copy()

    # End and clear check - return 1
    if len(counts_copy) == 0:
        if "#" in springs[i:]:
            return 0
        
        return 1

    # End check of iteration, final check
    if i >= len(springs):
        if cur_group_count == counts_copy[-1]:
            counts_copy.pop()
            if len(counts_copy) == 0:
                return 1
        return 0

    # check if current group is too large or valid
    if springs[i] != "#":
        if cur_group_count > counts_copy[-1]:
            return 0
        
        elif cur_group_count == counts_copy[-1]:
            counts_copy.pop()
            cur_group_count = 0
            skip = True

    # if we hit a dot and the current group doesn't work, return 0
    if springs[i] == ".":
        if cur_group_count > 0 and cur_group_count < counts_copy[-1]:
            return 0

        i += 1
        return recurse_springs(springs, counts_copy, i, cur_group_count)

    # if we hit #, iterate and move on 
    elif springs[i] == "#":
        cur_group_count += 1

        return recurse_springs(springs, counts_copy, i + 1, cur_group_count)

    # if ?, recurse with each possibility (. or #)
    elif springs[i] == "?":
        p_springs = springs[:i] + "." + springs[i + 1 :]
        if skip:
            return recurse_springs(p_springs, counts_copy, i, cur_group_count)
        else:
            s_springs = springs[:i] + "#" + springs[i + 1 :]

            return recurse_springs(
                p_springs, counts_copy, i, cur_group_count
            ) + recurse_springs(s_springs, counts_copy, i, cur_group_count)


possible_springs = []

with open("2023_python/day12/input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        springs_row, spring_count_list = parse_data(line)
        n = recurse_springs(springs_row, spring_count_list)

        possible_springs.append(n)

print(sum(possible_springs))
