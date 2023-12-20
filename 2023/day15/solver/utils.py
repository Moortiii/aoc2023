from typing import Generator


def read_lines(input_file: str):
    with open(input_file) as f:
        return f.read()


def read_numbers(input_file: str):
    with open(input_file) as f:
        return [int(num) for num in f.read().split(",")]


def sliding_window(
    array: list, window: int, step: int | None = None
) -> Generator[list, None, None]:
    if step is None:
        step = window

    for i in range(0, len(array) - window + 1, step):
        yield array[i : i + window]


def out_of_bounds(row: int, col: int, matrix: list[list]):
    if row < 0 or row >= len(matrix):
        return True

    if col < 0 or col >= len(matrix[0]):
        return True

    return False


def get_adjacent(
    row: int, col: int, matrix: list[list], width: int = 1, height: int = 1
) -> tuple[int, int]:
    skip_positions = [(row + i, col + j) for i in range(height) for j in range(width)]
    adjacent = []
    for i in range(row - 1, row + 1 + height):
        for j in range(col - 1, col + 1 + width):
            # Skip current position
            if (i, j) in skip_positions:
                continue

            # Check if out of bounds
            if out_of_bounds(row, col, matrix):
                continue

            adjacent.append((i, j))

    return adjacent
