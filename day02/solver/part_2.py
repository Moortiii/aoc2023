from collections import defaultdict
from functools import reduce

from solver import utils


def solve(input_file: str):
    lines = utils.read_lines(input_file)

    gem_bags = {}

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

        gem_bags[game_id] = gem_bag

    powers = []

    for game_id, gem_bag in gem_bags.items():
        power = reduce(lambda x, y: x * y, gem_bag.values())
        powers.append(power)

    return sum(powers)
