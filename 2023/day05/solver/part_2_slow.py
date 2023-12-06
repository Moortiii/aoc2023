import re
from collections import defaultdict

from solver import utils


def split(arr, chunk_size):
    for i in range(0, len(arr), chunk_size):
        yield arr[i : i + chunk_size]


def solve(input_file: str):
    lines = utils.read_lines(input_file)

    seeds = list(map(int, [num for num in re.findall(r"\d+", lines[0])]))

    seed_pairs = list(split(seeds, chunk_size=2))

    seeds = []

    for seed_pair in seed_pairs:
        seeds.extend(list(range(seed_pair[0], seed_pair[0] + seed_pair[1])))

    seed_pairs = [seeds[i : i + 1 : 3] for i in range(len(seeds))]

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

    for category, ranges in mapping.items():
        print("Category:", category)
        for src, dst in ranges:
            print(src, dst)

        print()

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

    print(locations)
    print(min(locations))
