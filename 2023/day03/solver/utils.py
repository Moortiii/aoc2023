from typing import Generator


def read_lines(input_file: str):
    with open(input_file) as f:
        return [line.strip() for line in f.readlines()]


def read_numbers(input_file: str):
    with open(input_file) as f:
        return [int(num) for num in f.read().split(",")]


def create_matrix(lines: list[str]):
    rows = []

    for line in lines:
        row = []

        for char in line:
            row.append(char)

        rows.append(row)

    return rows


def sliding_window(
    array: list, window: int, step: int | None = None
) -> Generator[list, None, None]:
    if step is None:
        step = window

    for i in range(0, len(array) - window + 1, step):
        yield array[i : i + window]


def get_adjacent(arr: list, i: int, j: int, with_index: bool = False):
    N = len(arr)
    M = len(arr[0])

    def within_bounds(i: int, j: int):
        return not (i < 0 or j < 0 or (i > N - 1) or (j > M - 1))

    adjacent = []

    bounds = [
        (i - 1, j - 1),
        (i - 1, j),
        (i - 1, j + 1),
        (i, j - 1),
        (i, j + 1),
        (i + 1, j - 1),
        (i + 1, j),
        (i + 1, j + 1),
    ]

    for bound in bounds:
        x, y = bound

        if within_bounds(x, y):
            if with_index:
                adjacent.append((arr[x][y], (x, y)))
            else:
                adjacent.append(arr[x][y])

    return adjacent
