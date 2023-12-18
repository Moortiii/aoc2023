from solver import utils


def solve(input_file: str):
    rows = utils.read_lines(input_file)
    rows = [list(row) for row in rows]

    rows = list(zip(*rows[::-1]))

    for j, row in enumerate(rows):
        row = list(row)

        i = len(row) - 1

        while i > 0:
            if row[i] == ".":
                if row[i - 1] == "O":
                    row[i] = "O"
                    row[i - 1] = "."

                    i = len(row)

            i -= 1

        rows[j] = row

    # Rotate back to original
    rows = list(zip(*rows[::-1]))
    rows = list(zip(*rows[::-1]))
    rows = list(zip(*rows[::-1]))

    load = 0

    for i, row in enumerate(rows[::-1]):
        row = list(row)
        rock_count = len([x for x in row if x == "O"])
        load += rock_count * (i + 1)

    return load
