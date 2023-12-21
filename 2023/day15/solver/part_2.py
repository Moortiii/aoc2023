from solver import utils
from functools import reduce
from collections import defaultdict


def HASH(instruction):
    current_value = 0

    for char in instruction:
        current_value += ord(char)
        current_value *= 17
        current_value = current_value % 256

    return current_value


def solve(input_file: str):
    instructions = utils.read_lines(input_file)
    instructions = instructions.split(",")

    labels = defaultdict(list)
    lenses = defaultdict(list)

    for instruction in instructions:
        if "-" in instruction:
            label = instruction[:-1]
            box_number = HASH(label)

            try:
                index = labels[box_number].index(label)
                labels[box_number].pop(index)
                lenses[box_number].pop(index)
            except ValueError:
                pass
        else:
            label, focal_length = instruction.split("=")
            box_number = HASH(label)

            try:
                index = labels[box_number].index(label)
                lenses[box_number].pop(index)
                lenses[box_number].insert(index, focal_length)
            except ValueError:
                labels[box_number].append(label)
                lenses[box_number].append(focal_length)

    focusing_powers = []

    for box_number, box_labels in labels.items():
        for slot, label in enumerate(box_labels):
            focal_length = lenses[box_number][slot]
            focusing_power = (box_number + 1) * (slot + 1) * int(focal_length)
            focusing_powers.append(focusing_power)

    return reduce(lambda x, y: x + y, focusing_powers)
