from typing import Literal

from solver import utils

replacements = {
    "|": "║",
    "L": "╚",
    "J": "╝",
    "F": "╔",
    "-": "═",
    "7": "╗",
}

pipe_compatibility_chart = {
    "║": [
        "╚",
        "╝",
        "╔",
        "║",
        "═",
        "╗",
    ],
    "╚": ["║", "═", "╗", "╝"],
    "╝": ["═", ""],
}


pipe_compatibility_chart = {
    "║": {
        "down": "║",
        "down_left": "╝",
        "down_right": "╚",
        "up": "║",
        "up_right": "╔",
        "up_left": "╗",
        "left": None,
        "right": None,
    },
    "╚": {
        "down": None,
        "down_left": None,
        "down_right": None,
        "up": "║",
        "up_right": "╔",
        "up_left": "╗",
        "left": None,
        "right": "═",
    },
}


class Tile:
    def __init__(self, pipe: str, left: str, right: str, up: str, down: str):
        self.pipe = pipe
        self.left = left
        self.right = right
        self.up = up
        self.down = down

    def can_move(
        self,
        direction: Literal[
            "up",
            "down",
            "left",
            "right",
            "down_right",
            "down_left",
            "up_right",
            "up_left",
        ],
    ):
        ...


def solve(input_file: str):
    lines = utils.read_lines(input_file)

    with open("maze.txt", "w+") as f:
        for line in lines:
            for character, replacement in replacements.items():
                line = line.replace(character, replacement)

            print(line)

            f.write(f"{line}\n")
