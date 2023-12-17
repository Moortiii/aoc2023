import re

from solver import utils


def generate_permutations(pattern):
    if not pattern:
        return [""]

    permutations = []

    for sub_permutation in generate_permutations(pattern[1:]):
        if pattern[0] == "?":
            permutations.append("#" + sub_permutation)
            permutations.append("." + sub_permutation)
        else:
            permutations.append(pattern[0] + sub_permutation)

    return permutations


def solve(input_file: str):
    lines = utils.read_lines(input_file)

    total_arrangements = 0

    for line in lines:
        arrangements = set()
        springs, info = line.split(" ")

        info_split = list(map(int, info.split(",")))

        pattern = r"^\.*"

        for i, count in enumerate(info_split):
            if i == len(info_split) - 1:
                pattern += f"\#{{{count}}}\.*$"
            else:
                pattern += f"\#{{{count}}}\.+"

        for permutation in generate_permutations(springs):
            matches = re.findall(pattern=pattern, string=permutation)

            if matches:
                arrangements.add(permutation)

        total_arrangements += len(arrangements)

    return total_arrangements
