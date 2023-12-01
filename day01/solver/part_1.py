from solver import utils


def solve(input_file: str):
    lines = utils.read_lines(input_file)

    numbers = []

    for line in lines:
        digits = [int(c) for c in line if c.isdigit()]

        numbers.append(int(f"{digits[0]}{digits[-1]}"))

    return sum(numbers)
