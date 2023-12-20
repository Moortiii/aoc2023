from solver import utils
from functools import reduce

def solve(input_file: str):
    instructions = utils.read_lines(input_file)
    instructions = instructions.split(",")

    values = []

    for instruction in instructions:
        current_value = 0

        for char in instruction:
            current_value += ord(char)
            current_value *= 17
            current_value = current_value % 256

        values.append(current_value)
    
    return reduce(lambda x,y: x+y, values)
