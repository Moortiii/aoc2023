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

            line = list(map(int, [num for num in re.findall(r"\d+", line)]))
            dest_start, source_start, length = line

            dst_range = range(dest_start, dest_start + length)
            src_range = range(source_start, source_start + length)

            mapping[category].append((src_range, dst_range))

    categories = [
        "seed_to_soil",
        "soil_to_fertilizer",
        "fertilizer_to_water",
        "water_to_light",
        "light_to_temp",
        "temp_to_humidty",
        "humidity_to_location",
    ]

    locations = []

    for seed in seeds:
        _next = seed

        for category in categories:
            for src, dst in mapping[category]:
                if _next in src:
                    _next = dst[0] + src.index(_next)
                    break
            else:
                _next = _next

        locations.append(_next)

    return min(locations)
