from __future__ import annotations

import uuid
from collections import defaultdict
from solver import utils
from typing import Literal

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

    def print_position(self):
        current_tile = self.tiles[self.x][self.y].beam_type

        print(
            f"{self.id[:5]}: Current '{current_tile}' @ ({self.x}, {self.y}) -> "
            f"{self.direction} "
        )

    def add_beam(self, direction, x: int | None = None, y: int | None = None):
        if x is None:
            x = self.x

        if y is None:
            y = self.y

        if x > MAX_WIDTH or x < 0:
            return

        if y > MAX_HEIGHT or y < 0:
            return

        beam = Beam(x=x, y=y, beams=self.beams, tiles=self.tiles, direction=direction)
        self.beams.append(beam)

        print(f"{beam.id[:5]}: Spawned beam at ({x}, {y}) going {direction}...")

    def update_position(self):
        if self.stopped:
            return

        # self.print_position()

        if self.tiles[self.x][self.y].label == ".":
            self.tiles[self.x][self.y].label = direction_map[self.direction]

        # self.tiles[self.x][self.y].label = "#"

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
                    self.add_beam(direction="up", x=self.x + 1, y=self.y - 1)
                    self.add_beam(direction="down", x=self.x + 1, y=self.y + 1)
                    # print(f"{self.id[:5]}: Split at ({self.x}, {self.y})\n")
                    self.stopped = True
                case "-":
                    self.x = self.x + 1
                case ".":
                    self.x = self.x + 1

            print(
                f"{self.id[:5]}: Next tile '{next_tile.beam_type}' @ ({next_tile.x},{next_tile.y}) -> {self.direction}"
            )
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
                    print(f"Splitting {self.id[:5]} at ({self.x}, {self.y})")
                    self.add_beam(x=self.x - 1, y=self.y - 1, direction="up")
                    self.add_beam(x=self.x - 1, y=self.y + 1, direction="down")
                    self.stopped = True
                case "-":
                    self.x = self.x - 1
                case ".":
                    self.x = self.x - 1

            print(
                f"{self.id[:5]}: Next tile '{next_tile.beam_type}' @ ({next_tile.x},{next_tile.y}) -> {self.direction}"
            )

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
                    print(f"Splitting {self.id[:5]} at ({self.x}, {self.y})")
                    self.add_beam(direction="left", y=self.y - 1)
                    self.add_beam(direction="right", y=self.y - 1)
                    self.stopped = True
                case ".":
                    self.y = self.y - 1

            print(
                f"{self.id[:5]}: Next tile '{next_tile.beam_type}' @ ({next_tile.x},{next_tile.y}) -> {self.direction}"
            )
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
                    print(f"Splitting {self.id[:5]} at ({self.x}, {self.y})")
                    self.add_beam(direction="left", y=self.y + 1)
                    self.add_beam(direction="right", y=self.y + 1)
                    self.stopped = True
                case ".":
                    self.y = self.y + 1

            print(
                f"{self.id[:5]}: Next tile '{next_tile.beam_type}' @ ({next_tile.x},{next_tile.y}) -> {self.direction}"
            )
        else:
            raise ValueError("You fucked up")

        if not self.stopped:
            self.print_position()


class Tile:
    def __init__(self, x: int, y: int, beam_type: Literal[".", "|", "/", "\\", "-"]):
        self.x = x
        self.y = y
        self.label = beam_type
        self.beam_type = beam_type
        self.energized = False


def solve(input_file: str):
    global MAX_HEIGHT
    global MAX_WIDTH

    lines = utils.read_lines(input_file)

    def infinite_defaultdict():
        return defaultdict(infinite_defaultdict)

    tiles = infinite_defaultdict()

    for y, line in enumerate(lines):
        MAX_HEIGHT = y

        for x, char in enumerate(line):
            MAX_WIDTH = x
            tiles[x][y] = Tile(x=x, y=y, beam_type=char)

    initial_beam = Beam(x=0, y=0, direction="right", beams=[], tiles=tiles)
    beams: list[Beam] = [initial_beam]
    initial_beam.beams = beams

    # while not all(beam.stopped for beam in beams):
    for _ in range(100):
        for beam in beams:
            beam.update_position()

        print()

        for y in range(len(lines)):
            for x in range(len(lines[0])):
                print(tiles[x][y].label, end="")

            print()

        # print(
        # "Number of active beams:",
        # len([beam for beam in beams if not beam.stopped]),
        # )
