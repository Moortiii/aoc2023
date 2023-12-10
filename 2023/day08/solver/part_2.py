from dataclasses import dataclass

from solver import utils


@dataclass
class Node:
    left: str
    right: str


def solve(input_file: str):
    lines = utils.read_lines(input_file)

    original_instructions = list(lines[0])

    desert_map: dict[str, Node] = {}

    for line in lines[2:]:
        desert_map[line[0:3]] = Node(left=line[7:10], right=line[12:15])

    current_position = "AAA"

    instructions = original_instructions.copy()

    steps = 0

    # print("Instructions:", instructions)

    while current_position != "ZZZ":
        if instructions == []:
            instructions = original_instructions.copy()

        next_instruction = instructions.pop(0)
        # print("Next instruction", next_instruction)

        if next_instruction == "L":
            next_position = desert_map[current_position].left
            # print(f"{current_position} --(L)-> {next_position}")
        else:
            next_position = desert_map[current_position].right
            # print(f"{current_position} --(R)-> {next_position}")

        current_position = next_position

        steps += 1

        if steps % 1_000_000 == 0 and steps != 0:
            print(f"Steps: {steps}")

    print("Steps taken:", steps)
    return steps


if __name__ == "__main__":
    solve("./task_input/input.txt")
