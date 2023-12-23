from solver import utils
from collections import defaultdict
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

    max_height = 0
    min_height = 999999999
    max_width = 0
    min_width = 999999999

    position = (0, 0)
    tiles = defaultdict(lambda: defaultdict(list))

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

            if y < min_height:
                min_height = y

            if x > max_width:
                max_width = x

            if y > max_height:
                max_height = y

    cubic_meters = 0

    for y in range(min_height, max_height + 1):
        min_x = 999999
        max_x = 0

        for x in range(min_width, max_width + 1):
            if "#" in tiles[x][y]:
                if x < min_x:
                    min_x = x

                if x > max_x:
                    max_x = x

        span = len(range(min_x, max_x + 1))
        print("Span:", span)
        cubic_meters += span

    print("Dimensions:", min_width, max_width, min_height, max_height)

    # print_board(
    #     min_width=min_width,
    #     min_height=min_height,
    #     max_width=max_width,
    #     max_height=max_height,
    #     tiles=tiles,
    # )
    print("Cubic meters:", cubic_meters)
    return cubic_meters
