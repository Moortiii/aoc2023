from solver import utils


def solve(input_file: str):
    lines = utils.read_lines(input_file)

    rows = []

    for line in lines:
        row = []

        for char in line:
            row.append(char)

        rows.append(row)

    parts = []

    current_number = ""
    can_add = False

    for j, row in enumerate(rows):
        for i, current_char in enumerate(row):
            adjacent = utils.get_adjacent(rows, j, i)

            if not current_char.isdigit() and can_add:
                if current_number == "":
                    continue

                parts.append(int(current_number))
                current_number = ""
                can_add = False
                continue

            if not current_char.isdigit():
                current_number = ""
                continue

            current_number += current_char

            if not all(char.isdigit() or char == "." for char in adjacent):
                can_add = True

            if i == (len(rows[0]) - 1) and can_add:
                parts.append(int(current_number))
                can_add = False

        current_number = ""

    return sum(parts)
