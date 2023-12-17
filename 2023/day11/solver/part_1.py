import itertools

from solver import utils


def print_galaxies(lines: list[str]):
    for i, line in enumerate(lines):
        print(f"{i:3}", "".join(line))


def solve(input_file: str):
    lines = list(map(list, utils.read_lines(input_file)))

    for i, line in reversed(list(enumerate(lines.copy()))):
        galaxy_found = False

        for c in line:
            if c == "#":
                galaxy_found = True

        if not galaxy_found:
            lines.insert(i, ["."] * len(lines[0]))

    # Rotate once
    lines = list(zip(*lines[::-1]))

    for i, line in reversed(list(enumerate(lines.copy()))):
        galaxy_found = False

        for c in line:
            if c == "#":
                galaxy_found = True

        if not galaxy_found:
            lines.insert(i, ["."] * len(lines[0]))

    # Rotate back to original position
    lines = list(zip(*lines[::-1]))
    lines = list(zip(*lines[::-1]))
    lines = list(zip(*lines[::-1]))

    coordinates = []

    for i, row in enumerate(lines):
        for j, column in enumerate(row):
            if column == "#":
                coordinates.append((j, i))

    combinations = itertools.combinations(coordinates, r=2)

    total_distance = 0

    for i, combination in enumerate(combinations):
        a, b = combination
        difference = (abs(b[0] - a[0]), abs(b[1] - a[1]))
        total_distance += difference[0] + difference[1]

    return total_distance
