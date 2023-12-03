import re

from solver import utils


def solve(input_file: str):
    lines = utils.read_lines(input_file)
    rows = utils.create_matrix(lines)

    numbers = []

    for j, line in enumerate(lines):
        matches = re.finditer(r"(\d+)", line)

        for match in matches:
            numbers.append(
                (
                    int(match.groups()[0]),
                    [(j, i) for i in range(match.start(), match.end())],
                )
            )

    gear_acc = 0

    for j, row in enumerate(rows):
        for i, current_char in enumerate(row):
            if current_char != "*":
                continue

            adjacent = utils.get_adjacent(rows, j, i, with_index=True)

            indices = []

            for char in adjacent:
                if char[0].isdigit():
                    indices.append(char)

            picked = set()

            for index in indices:
                index = index[1]

                for i, entry in enumerate(numbers):
                    _, positions = entry

                    if any(index == position for position in positions):
                        picked.add(i)

            if len(picked) != 2:
                continue

            num_1 = numbers[picked.pop()][0]
            num_2 = numbers[picked.pop()][0]

            gear_acc += num_1 * num_2

    return gear_acc
