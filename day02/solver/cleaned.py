import re
from collections import defaultdict
from functools import reduce

from solver import utils


def read_input(input_file: str):
    lines = utils.read_lines(input_file)
    lines = [re.sub(r"Game \d+:", "", line).strip() for line in lines]
    lines = [line.replace(",", "").strip() for line in lines]
    lines = [line.replace(" ", "") for line in lines]
    lines = [re.sub(r"(\d+) ([a-z])+", r"\1\2", line) for line in lines]
    lines = [entry.split(";") for entry in lines]
    return lines


patterns = [(color, rf"(\d+){color}") for color in "rgb"]


def solve_cleaned(input_file: str):
    lines = read_input(input_file)

    gem_bags = []

    for line in lines:
        gem_bag = defaultdict(list)

        for showing in line:
            for color, pattern in patterns:
                count = re.findall(pattern, showing)

                if not count:
                    continue

                gem_bag[color].append(int(count.pop()))

        gem_bags.append(gem_bag)

    powers = []

    for gem_bag in gem_bags:
        powers.append(
            reduce(lambda x, y: x * y, [max(gem_bag[color]) for color in "rgb"])
        )

    return sum(powers)
