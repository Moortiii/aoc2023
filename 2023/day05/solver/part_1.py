import re
from collections import defaultdict

from solver import utils


def solve(input_file: str):
    lines = utils.read_lines(input_file)

    seeds = list(map(int, [num for num in re.findall(r"\d+", lines[0])]))

    current_line = 3

    categories = [
        "seed_to_soil",
        "soil_to_fertilizer",
        "fertilizer_to_water",
        "water_to_light",
        "light_to_temp",
        "temp_to_humidty",
        "humidity_to_location",
    ]

    category = categories.pop(0)

    mapping = defaultdict(list)

    for i, line in enumerate(lines[current_line:]):
        if line.strip() == "":
            category = categories.pop(0)
        else:
            if not any(c.isnumeric() for c in line):
                continue

            mapping[category].append(
                list(map(int, [num for num in re.findall(r"\d+", line)]))
            )

    for category, _lines in mapping.items():
        print("Category:", category)
        for line in _lines:
            dest_start, source_start, length = line
            print(
                line,
                range(dest_start, dest_start + length),
                range(source_start, source_start + length),
            )

        print()

    print("Seeds:", seeds)
