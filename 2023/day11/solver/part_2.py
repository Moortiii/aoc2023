import itertools

from solver import utils


def solve(input_file: str, expansion_factor: int):
    lines = list(map(list, utils.read_lines(input_file)))

    expanded_rows = set()

    for i, line in reversed(list(enumerate(lines.copy()))):
        galaxy_found = False

        for c in line:
            if c == "#":
                galaxy_found = True

        if not galaxy_found:
            expanded_rows.add(i)

    # Rotate once
    lines = list(zip(*lines[::-1]))

    expanded_columns = set()

    for i, line in reversed(list(enumerate(lines.copy()))):
        galaxy_found = False

        for c in line:
            if c == "#":
                galaxy_found = True

        if not galaxy_found:
            expanded_columns.add(i)

    # Rotate back to original position
    lines = list(zip(*lines[::-1]))
    lines = list(zip(*lines[::-1]))
    lines = list(zip(*lines[::-1]))

    coordinates = []

    for y, row in enumerate(lines):
        for x, column in enumerate(row):
            if column == "#":
                _expanded_rows = [_ for _ in range(0, y + 1) if _ in expanded_rows]
                _expanded_columns = [
                    _ for _ in range(0, x + 1) if _ in expanded_columns
                ]

                _x = x + (len(_expanded_columns) * (expansion_factor - 1))
                _y = y + (len(_expanded_rows) * (expansion_factor - 1))

                coordinates.append(
                    (
                        _x,
                        _y,
                    )
                )

    combinations = itertools.combinations(coordinates, r=2)

    total_distance = 0

    for i, combination in enumerate(combinations):
        a, b = combination
        difference = abs(b[0] - a[0]), abs(b[1] - a[1])
        total_distance += (difference[0]) + (difference[1])

    return total_distance
