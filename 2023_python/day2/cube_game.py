import re

# raw_games = open("2023_python/day2/example.txt", "r").read() # games 1, 2 & 5 pass. sum 8
raw_games = open("2023_python/day2/input.txt", "r").read()
raw_games = re.split("\n", raw_games)

limit = {"red": 12, "green": 13, "blue": 14} # limit set by challenge 

# format data to be easily iterable
def format_games_arr(games):
    formatted_game = {}

    for game in games:
        sets = re.split("[;:]\s+", game)
        game_num = sets[0][5:]

        sets = sets[1:]
        formatted_game[game_num] = []

        i = 0
        while i < len(sets):
            formatted_game[game_num].append({})
            set = re.split(",\s",sets[i])
            for color in set:
                color_data = re.split("\s", color)
                formatted_game[game_num][i][color_data[1]] = color_data[0]

            i += 1

    return formatted_game

# check if set in game is valid
def valid_set(set, limit):
    is_valid = True
    for color in limit:
        if set.get(color):
            if int(set[color]) > limit[color]:
                is_valid = False

    return is_valid

# check if game is possible
def possible_game(game, limit):
    possible = True
    for set in game:
        if not valid_set(set, limit):
            possible = False


    return possible

# gets possible game ids 
def possible_games(games, limit):
    possible_games = []
    for game_id in games:
        if possible_game(games[game_id], limit):
            possible_games.append(game_id)

    return possible_games

# returns the sum of all valid game ids
def sum_games(games):
    sum = 0
    for val in games:
        sum += int(val)
    
    return sum

games = format_games_arr(raw_games) # format games
possible_games_arr = possible_games(games, limit) # get all possible ids
print(sum_games(possible_games_arr)) # print sum of all possible ids

# gets the fewest possible cubes for each game
def fewest_cubes(games):
    fewest_cubes = []

    for game_id in games:
        cubes = {"red": 1, "blue": 1, "green": 1}
        for set in games[game_id]:
            for color in set:
                if int(set[color]) > cubes[color]:
                    cubes[color] = int(set[color])
        
        fewest_cubes.append(list(cubes.values()))

    return fewest_cubes

# builds array of the power of each set of cubes
def power_of_cubes(cubes):
    powers = []
    for vals in cubes:
        power = 1
        for val in vals:
            power *= val
        powers.append(power)

    return powers
        

fewest_cubes_arr = fewest_cubes(games) # get fewest cubes
fewest_cubes_powers = power_of_cubes(fewest_cubes_arr) # get powers for each set
powers_sum = sum_games(fewest_cubes_powers) # sum the powers

print(powers_sum)