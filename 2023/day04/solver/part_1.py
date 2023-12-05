import re

from solver import utils


def solve(input_file: str):
    lines = utils.read_lines(input_file)
    lines = [line.replace(" | ", "|") for line in lines]
    lines = [re.sub(r"Card.+?\d+: ", "", line) for line in lines]

    lines = [line.split("|") for line in lines]

    score = 0

    for winning_numbers, scratched in lines:
        matches = []
        scratched = list(map(int, re.findall(r"\d+", scratched)))
        winning_numbers = list(map(int, re.findall(r"\d+", winning_numbers)))

        for number in scratched:
            if number in winning_numbers:
                matches.append(number)

        if len(matches) == 1:
            score += 1
        elif len(matches) == 0:
            continue
        else:
            score += 1 * (2 ** (len(matches) - 1))

    return score
