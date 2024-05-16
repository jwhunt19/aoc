def parse_data(line: str) -> tuple[str, list[int]]:
    springs, groups = line.split()
    groups = [int(x) for x in groups.split(",")]
    groups = tuple(groups)

    # Part 2 modification (unfold)
    springs = "?".join([springs] * 5)
    groups = groups * 5

    return springs, groups


def recurse_springs(
    springs: str, groups: tuple[int], memo: dict[tuple[str, tuple[int]]] = {}
) -> int:

    s_key = (springs, groups)
    if s_key in memo:
        return memo[s_key]

    # If all groups accounted for and no more # left, return 1 valid arrangement
    if len(groups) == 0:
        if "#" in springs:
            return 0

        return 1

    # If end of springs str and all groups accounted for, return 1 valid arrangment
    if len(springs) == 0:
        if len(groups) != 0:
            return 0

        return 1

    result = 0

    # If char isn't #, recurse treating ?'s as a dot .
    if springs[0] != "#":
        dot_key = (springs[1:], groups)
        memo[dot_key] = recurse_springs(springs[1:], groups, memo)
        result += memo[dot_key]

    # if char is # or ?, check for valid group match and recurse
    if springs[0] == "#" or springs[0] == "?":
        ls = len(springs)  # len of springs
        g = groups[0]  # group
        if g <= ls and "." not in springs[:g] and (ls == g or springs[g] != "#"):
            spring_key = (springs[g + 1 :], groups[1:])
            memo[spring_key] = recurse_springs(springs[g + 1 :], groups[1:], memo)
            result += memo[spring_key]

    return result


possible_springs = 0

with open("2023_python/day12/input.txt", encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        springs_str, spring_groups = parse_data(line)

        possible_springs += recurse_springs(springs_str, spring_groups)


print(possible_springs)
