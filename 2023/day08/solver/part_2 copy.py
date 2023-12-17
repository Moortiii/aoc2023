from collections import defaultdict
from dataclasses import dataclass
from functools import reduce

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

    instructions = original_instructions.copy()

    paths = defaultdict(list)
    paths_to_trace = [key for key in desert_map.keys() if key[2] == "A"]

    print()
    print("Paths to trace:", paths_to_trace)

    for path in paths_to_trace:
        current_position = path

        # print("Current position:", current_position)

        steps = 1
        loops = 0

        i = 0

        while i < 1_000_000:
            if instructions == []:
                instructions = original_instructions.copy()
                loops += 1
                print(f"Looping around after {steps} steps..")

            next_instruction = instructions.pop(0)
            # print("Next instruction", next_instruction)

            if next_instruction == "L":
                next_position = desert_map[current_position].left
                # print(f"{current_position} --(L)-> {next_position}")
            else:
                next_position = desert_map[current_position].right
                # print(f"{current_position} --(R)-> {next_position}")

            # print("Steps taken:", steps)

            current_position = next_position

            if current_position[2] == "Z":
                print(
                    f"Reached destination in {steps} steps after {loops} loops for {path}"
                )
                paths[path] = steps
                break

            steps += 1

        print("Ended up at:", current_position, "after", steps, "steps")
        print()

    print("Paths:", paths)
    return reduce(lambda x, y: x * y, paths.values())


if __name__ == "__main__":
    solve("./task_input/input.txt")
