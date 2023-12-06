from functools import reduce

from solver import utils


def solve(input_file: str):
    lines = utils.read_lines(input_file)

    times = list(map(int, lines[0].split()[1:]))
    distances = list(map(int, lines[1].split()[1:]))

    total_options = []

    for time, distance in zip(times, distances):
        options = 0

        for i in range(time):
            remaining = time - i
            traveled = i * remaining

            if traveled > distance:
                options += 1

        total_options.append(options)

    return reduce(lambda x, y: x * y, total_options)
