import re
from collections import defaultdict

from solver import utils


def solve(input_file: str):
    lines = utils.read_lines(input_file)
    lines = [line.replace(" | ", "|") for line in lines]
    lines = [re.sub(r"Card.+?\d+: ", "", line) for line in lines]
    lines = [line.split("|") for line in lines]

    card_bag = defaultdict(int)

    for card_number, line in enumerate(lines):
        card_number += 1
        card_bag[card_number] += 1

        winning_numbers, scratched = line

        scratched = list(map(int, re.findall(r"\d+", scratched)))
        winning_numbers = list(map(int, re.findall(r"\d+", winning_numbers)))

        matches = [number for number in scratched if number in winning_numbers]

        for _ in range(card_bag[card_number]):
            for i in range(card_number + 1, card_number + len(matches) + 1):
                card_bag[i] += 1

    return sum(card_bag.values())
