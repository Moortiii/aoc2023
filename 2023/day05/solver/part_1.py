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

    for category, ranges in mapping.items():
        print("Category:", category)
        for src, dst in ranges:
            print(src, dst)

        print()

    for seed in seeds:
        for src, dst in mapping["seed_to_soil"]:
            if seed in src:
                print(
                    seed,
                    "in",
                    src,
                    "at index",
                    src.index(seed),
                    "corresponding soil is at",
                    dst[0] + src.index(seed),
                )
                break
        else:
            print(seed, "not in", src, "therefore corresponding soil is at", seed)
