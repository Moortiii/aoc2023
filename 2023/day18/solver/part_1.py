from solver import utils
from collections import defaultdict


class Map:
    def __init__(
        self,
        tiles,
        max_width: int,
        min_width: int,
        min_height: int,
        max_height: int,
    ):
        self.tiles = tiles
        self.max_height = max_height
        self.min_height = min_height
        self.max_width = max_width
        self.min_width = min_width

    def print(self):
        for y in range(self.min_height, self.max_height + 1):
            for x in range(self.min_width, self.max_width + 1):
                if "#" in self.tiles[x][y]:
                    print("#", end="")
                elif "-" in self.tiles[x][y]:
                    print("-", end="")
                else:
                    print(".", end="")

            print()


def solve(input_file: str, starting_point: tuple[int, int] | None = None):
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

    if starting_point is None:
        starting_point = (150, -72)

    _map = Map(
        tiles=tiles,
        max_width=max_width,
        min_width=min_width,
        min_height=min_height,
        max_height=max_height,
    )

    override = "#"

    utils.floodfill(
        start_x=starting_point[0],
        start_y=starting_point[1],
        max_height=max_height,
        min_height=min_height,
        min_width=min_width,
        max_width=max_width,
        override=override,
        tiles=tiles,
    )

    _map.print()

    cubic_meters = 0

    for y in range(min_height, max_height + 1):
        for x in range(min_width, max_width + 1):
            if override in tiles[x][y]:
                cubic_meters += 1

    return cubic_meters


if __name__ == "__main__":
    # solve("./task_input/test_1.txt", (2, 1))
    output = solve("./task_input/input.txt", (150, -72))
    print("Part 1 solution:", output)
