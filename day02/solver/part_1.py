from collections import defaultdict

from solver import utils


def solve(input_file: str):
    lines = utils.read_lines(input_file)

    matching_games = []

    for line in lines:
        gem_bag = defaultdict(int)

        game_id, gems = line.split(":")
        game_id = int(game_id.replace("Game ", ""))

        gem_showings = [entry.strip() for entry in gems.split(";")]

        for showing in gem_showings:
            showing = showing.split(",")
            showing = [entry.strip() for entry in showing]

            for gem in showing:
                count, color = gem.split(" ")
                count = int(count)

                if gem_bag[color] < count:
                    gem_bag[color] = count

        if gem_bag["red"] <= 12 and gem_bag["green"] <= 13 and gem_bag["blue"] <= 14:
            matching_games.append(game_id)

    return sum(matching_games)
