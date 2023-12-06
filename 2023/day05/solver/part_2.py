"""
The number of seeds to process is far too large to fit into memory, so we must employ
some other technique or optimalization.

Ideas:

1) Find the lowest number in all of the ranges, and check if this is within the range
    of any of the humidity-to-location ranges. If a number isn't present in any of the
    ranges, it's seed value will also correspond with its location value. If this value
    is lower than the minimum value of all of the ranges, it is the correct solution.

2) Are there overlapping ranges that we can discard entirely?

3) Use overlapping to find shared numbers across ranges to shrink the search space.

"""
import re
from collections import defaultdict

from solver import utils


def range_overlap(range1, range2):
    return range(max(range1[0], range2[0]), min(range1[-1], range2[-1]) + 1)


def range_subset(range1, range2):
    """Whether range1 is a subset of range2."""
    if not range1:
        return True  # empty range is subset of anything
    if not range2:
        return False  # non-empty range can't be subset of empty range
    if len(range1) > 1 and range1.step % range2.step:
        return False  # must have a single value or integer multiple step
    return range1.start in range2 and range1[-1] in range2


def split(arr, chunk_size):
    for i in range(0, len(arr), chunk_size):
        yield arr[i : i + chunk_size]


def solve(input_file: str):
    lines = utils.read_lines(input_file)
    seeds = list(map(int, [num for num in re.findall(r"\d+", lines[0])]))

    seed_pairs = list(split(seeds, chunk_size=2))
    seed_ranges = []

    for seed_pair in seed_pairs:
        seed_ranges.append(range(seed_pair[0], seed_pair[0] + seed_pair[1]))

    print(seed_ranges)

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

    for line in lines[current_line:]:
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

    possible_ranges = set()

    for seed_range in seed_ranges:
        _next = seed_range

        for category in categories:
            for src, dst in mapping[category]:
                if range_overlap(_next, src):
                    print(
                        f"{_next} overlaps with {src} in category {category} -> {dst}"
                    )
                    _next = dst
                else:
                    print(
                        f"{_next} does not overlap with {src} in category {category} -> {_next}"
                    )

        print()
        possible_ranges.add(_next)

    print("Possible ranges:")
    print([_range for _range in possible_ranges])

    print("Length of possible ranges:")
    print([len(_range) for _range in possible_ranges])
