from solver import utils


def solve(input_file: str):
    lines = utils.read_lines(input_file)

    time = int("".join(lines[0].split()[1:]))
    distance = int("".join(lines[1].split()[1:]))

    options = 0

    for i in range(time):
        remaining = time - i
        traveled = i * remaining

        if traveled > distance:
            options += 1

    return options
