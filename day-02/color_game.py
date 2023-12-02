MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

def read_file_and_add_up_possible_ids(filepath):
    """see title"""

    games = parse_file(filepath)

    sum_of_ids = 0
    for game_id in games:
        if is_game_possible(games[game_id]):
            print(f'game {game_id} is possible')
            sum_of_ids += game_id

    return sum_of_ids

def read_file_and_add_up_powers(filepath):
    """find sum of all powers of games"""

    # for each game, find the max value for red, green, blue cubes
    # multiply them together
    # add to sum

    games = parse_file(filepath)

    sum_powers = 0

    for game_id in games:
        mins_necessary = get_mins_necessary(games[game_id])
        power = get_game_power(mins_necessary)
        print("power=", power)
        sum_powers += power

    return sum_powers

def get_mins_necessary(game):
    """"""

    red_min_nec = 0
    green_min_nec = 0
    blue_min_nec = 0

    for round in game:
        num_red = round.get("red",0)
        num_blue = round.get("blue", 0)
        num_green = round.get("green", 0)

        red_min_nec = num_red if num_red > red_min_nec else red_min_nec
        green_min_nec = num_green if num_green > green_min_nec else green_min_nec
        blue_min_nec = num_blue if num_blue > blue_min_nec else blue_min_nec

    min_requirements = [red_min_nec, green_min_nec, blue_min_nec]
    return min_requirements

def get_game_power(min_requirements):
    """"""

    power = 1
    for num in min_requirements:
        power *= num

    return power



def is_game_possible(game):
    """returns true is game is possible, false if not"""

    for round in game:
        if round.get("red", 0) > MAX_RED: return False
        if round.get("green", 0) > MAX_GREEN: return False
        if round.get("blue", 0) > MAX_BLUE: return False

    return True


def parse_file(filepath):

    game_id_to_rounds = {}

    with open(filepath, "r") as file:
        for line in file:
            line = line.strip()
            [game, rounds_as_string] = line.split(":")

            game_id = int(game.split(" ")[1])
            round_strings = rounds_as_string.split(";")

            # print("game", game_id)
            # print("round strings", round_strings)

            rounds = []
            for round in round_strings:
                round_colors_to_num = {}
                # print("round", round)

                colors = round.strip().split(",")
                for color in colors:
                    # print("color", color)
                    [num, color] = color.strip().split(" ")
                    round_colors_to_num[color] = int(num)

                rounds.append(round_colors_to_num)

            game_id_to_rounds[game_id] = rounds

    return game_id_to_rounds