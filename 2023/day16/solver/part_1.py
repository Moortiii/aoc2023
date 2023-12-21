from __future__ import annotations

import uuid
from collections import defaultdict
from solver import utils
from typing import Literal
from copy import deepcopy

MAX_WIDTH = 0
MAX_HEIGHT = 0


direction_map = {"down": "v", "up": "^", "left": "<", "right": ">"}


class Beam:
    def __init__(
        self,
        x: int,
        y: int,
        beams: list[Beam],
        tiles: dict[int, dict[int, Tile]],
        direction: Literal["left", "right", "up", "down"],
    ):
        self.x = x
        self.y = y
        self.id = str(uuid.uuid4())
        self.beams = beams
        self.tiles = tiles
        self.stopped = False
        self.direction = direction
        self.visited = []

    def print_position(self):
        current_tile = self.tiles[self.x][self.y].beam_type

        print(
            f"{self.id[:5]}: Current '{current_tile}' @ ({self.x}, {self.y}) -> "
            f"{self.direction} "
        )

    def print_next_tile(self, next_tile: Tile):
        print(
            f"{self.id[:5]}: Next tile '{next_tile.beam_type}' @ ({next_tile.x},{next_tile.y}) -> {self.direction}"
        )

    def add_beam(self, direction, x: int | None = None, y: int | None = None):
        if x is None:
            x = self.x

        if y is None:
            y = self.y

        if x > MAX_WIDTH or x < 0 or y > MAX_HEIGHT or y < 0:
            return

        beam = Beam(x=x, y=y, beams=self.beams, tiles=self.tiles, direction=direction)
        # print(f"{beam.id[:5]}: Spawned beam at ({x}, {y}) going {direction}...")
        self.beams.append(beam)

    def update_position(self):
        current_tile = self.tiles[self.x][self.y]
        current_tile.energized = True

        if current_tile.label == ".":
            current_tile.label = direction_map[self.direction]

        if self.stopped:
            return

        if self.direction == "right":
            next_tile = self.tiles[self.x + 1][self.y]

            if not isinstance(next_tile, Tile):
                self.stopped = True
                return

            next_char = next_tile.beam_type

            match next_char:
                case "/":
                    self.x = self.x + 1
                    self.direction = "up"
                case "\\":
                    self.x = self.x + 1
                    self.direction = "down"
                case "|":
                    self.add_beam(direction="up", x=self.x + 1)
                    self.add_beam(direction="down", x=self.x + 1)
                    self.stopped = True
                case "-":
                    self.x = self.x + 1
                case ".":
                    self.x = self.x + 1

            # self.print_next_tile(next_tile=next_tile)
        elif self.direction == "left":
            next_tile = self.tiles[self.x - 1][self.y]

            if not isinstance(next_tile, Tile):
                self.stopped = True
                return

            next_char = next_tile.beam_type

            match next_char:
                case "/":
                    self.x = self.x - 1
                    self.direction = "down"
                case "\\":
                    self.x = self.x - 1
                    self.direction = "up"
                case "|":
                    # print(f"Splitting {self.id[:5]} at ({self.x}, {self.y})")
                    self.add_beam(x=self.x - 1, direction="up")
                    self.add_beam(x=self.x - 1, direction="down")
                    self.stopped = True
                case "-":
                    self.x = self.x - 1
                case ".":
                    self.x = self.x - 1

            # self.print_next_tile(next_tile=next_tile)

        elif self.direction == "up":
            next_tile = self.tiles[self.x][self.y - 1]

            if not isinstance(next_tile, Tile):
                self.stopped = True
                return

            next_char = next_tile.beam_type

            match next_char:
                case "/":
                    self.direction = "right"
                    self.y = self.y - 1
                case "\\":
                    self.direction = "left"
                    self.y = self.y - 1
                case "|":
                    self.y = self.y - 1
                case "-":
                    # print(f"Splitting {self.id[:5]} at ({self.x}, {self.y})")
                    self.add_beam(direction="left", y=self.y - 1)
                    self.add_beam(direction="right", y=self.y - 1)
                    self.stopped = True
                case ".":
                    self.y = self.y - 1

            # self.print_next_tile(next_tile=next_tile)
        elif self.direction == "down":
            next_tile = self.tiles[self.x][self.y + 1]

            if not isinstance(next_tile, Tile):
                self.stopped = True
                return

            next_char = next_tile.beam_type

            match next_char:
                case "/":
                    self.direction = "left"
                    self.y = self.y + 1
                case "\\":
                    self.direction = "right"
                    self.y = self.y + 1
                case "|":
                    self.y = self.y + 1
                case "-":
                    # print(f"Splitting {self.id[:5]} at ({self.x}, {self.y})")
                    self.add_beam(direction="left", y=self.y + 1)
                    self.add_beam(direction="right", y=self.y + 1)
                    self.stopped = True
                case ".":
                    self.y = self.y + 1

            # self.print_next_tile(next_tile=next_tile)
        else:
            raise ValueError("You fucked up")

        # if not self.stopped:
        #    self.print_position()


class Tile:
    def __init__(self, x: int, y: int, beam_type: Literal[".", "|", "/", "\\", "-"]):
        self.x = x
        self.y = y
        self.label = beam_type
        self.beam_type = beam_type
        self.energized = False


def infinite_defaultdict():
    return defaultdict(infinite_defaultdict)


def print_tiles(lines, tiles, energized=False):
    print()

    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if energized:
                if tiles[x][y].energized:
                    print("#", end="")
                else:
                    print(tiles[x][y].label, end="")
            else:
                print(tiles[x][y].label, end="")

        print()


def solve(input_file: str):
    global MAX_HEIGHT
    global MAX_WIDTH

    lines = utils.read_lines(input_file)

    tiles = infinite_defaultdict()

    for y, line in enumerate(lines):
        MAX_HEIGHT = y

        for x, char in enumerate(line):
            MAX_WIDTH = x
            tiles[x][y] = Tile(x=x, y=y, beam_type=char)

    initial_beam = Beam(x=0, y=0, direction="right", beams=[], tiles=tiles)
    beams = [initial_beam]
    initial_beam.beams = beams

    counter = 0

    i = 0

    # for i in range(1000):
    while not all(beam.stopped for beam in beams):
        i += 1
        previous_tiles = deepcopy(tiles)

        for beam in beams:
            beam.update_position()

        # print_tiles(lines=lines, tiles=tiles)
        # print_tiles(lines=lines, tiles=tiles, energized=True)

        all_equal = True

        for y in range(len(lines)):
            for x in range(len(lines[0])):
                current = tiles[x][y]
                previous = previous_tiles[x][y]

                if current.label != previous.label:
                    all_equal = False
                    counter = 0

        if all_equal:
            counter += 1

        if counter >= 10:
            print(
                f"No changes detected in {counter} runs, final state reached after {i - counter} iterations"
            )
            break

    total_energized = 0

    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if tiles[x][y].energized:
                total_energized += 1

    return total_energized
