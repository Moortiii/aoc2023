from collections import defaultdict
from functools import reduce

from solver import utils


def get_differences(line: list[int]):
    return [j - i for i, j in zip(line[:-1], line[1:])]


def solve(input_file: str):
    lines = utils.read_lines(input_file)
    lines = [list(map(int, line.split())) for line in lines]

    oasis = defaultdict(list)

    for i, line in enumerate(lines):
        oasis[i].append(line)
        differences = get_differences(line)

        while not all(diff == 0 for diff in differences):
            oasis[i].append(differences)
            differences = get_differences(differences)

    history = []

    for diffs in oasis.values():
        diffs.reverse()

        for i, diff in enumerate(diffs):
            if i == 0:
                continue

            diff.append(diff[-1] + diffs[i - 1][-1])

        history.append(diff[-1])

    return reduce(lambda x, y: x + y, history)
