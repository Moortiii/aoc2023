from solver import utils
from collections import defaultdict
import re
from functools import reduce


def print_board(
    min_height: int, max_height: int, min_width: int, max_width: int, tiles
):
    for y in range(min_height, max_height + 1):
        for x in range(min_width, max_width + 1):
            print("#" if "#" in tiles[x][y] else ".", end="")

        print()


def solve(input_file: str):
    lines = utils.read_lines(input_file)

    max_height = float("-inf")
    min_height = float("inf")
    max_width = float("-inf")
    min_width = float("inf")

    position = (0, 0)
    tiles = defaultdict(lambda: defaultdict(dict))

    for line in lines:
        direction, length, color = line.split(" ")
        color = color.replace("(", "").replace(")", "")

        for _ in range(int(length)):
            x, y = position
            tiles[x][y] = color

            match direction:
                case "R":
                    x += 1
                case "L":
                    x -= 1
                case "U":
                    y -= 1
                case "D":
                    y += 1

            position = (x, y)

            if x < min_width:
                min_width = x
            if x > max_width:
                max_width = x
            if y < min_height:
                min_height = y
            if y > max_height:
                max_height = y

    cubic_meters = 0
    pattern = r"#{1,}\.*#{1,}\.*#{1,}|#{1,}\.*#{1,}|#{1,}#|#{1,}\.*#{1,}"

    for y in range(min_height, max_height + 1):
        row = "".join(
            [
                "#" if "#" in tiles[x][y] else "."
                for x in range(min_width, max_width + 1)
            ]
        )

        print(row)

        matches = list(re.finditer(string=row, pattern=pattern))

        print(matches)

        for match in matches:
            start, stop = match.span()
            cubic_meters += abs(start - stop)

    print()

    return cubic_meters
