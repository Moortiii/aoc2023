import multiprocessing
import re
import time
from collections import defaultdict
from datetime import datetime
from multiprocessing import Process

from solver import utils


def split(arr, chunk_size):
    for i in range(0, len(arr), chunk_size):
        yield arr[i : i + chunk_size]


def solve(input_file: str):
    lines = utils.read_lines(input_file)

    seeds = list(map(int, [num for num in re.findall(r"\d+", lines[0])]))
    seed_pairs = list(split(seeds, chunk_size=2))

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

    def calculate_locations(L: list, process_id: int, _range: range):
        locations = []

        seed_range = range(_range[0], _range[0] + _range[1])
        started = datetime.now()

        print(
            "Started process",
            process_id,
            "@",
            started,
            "for range of size",
            len(seed_range),
        )

        categories = [
            "seed_to_soil",
            "soil_to_fertilizer",
            "fertilizer_to_water",
            "water_to_light",
            "light_to_temp",
            "temp_to_humidty",
            "humidity_to_location",
        ]

        min_location = float("inf")

        for seed in seed_range:
            _next = seed

            for category in categories:
                for src, dst in mapping[category]:
                    if _next in src:
                        _next = dst[0] + src.index(_next)
                        break
                else:
                    _next = _next

            if _next < min_location:
                min_location = _next

        stopped = datetime.now()
        print(
            "Terminated process",
            process_id,
            "@",
            datetime.now(),
            "for range of size",
            len(seed_range),
        )
        print("Elapsed:", stopped - started)
        print()

        L.append(min_location)

    with multiprocessing.Manager() as manager:
        locations = manager.list()

        processes = []

        for i, seed_pair in enumerate(seed_pairs):
            p = Process(
                target=calculate_locations,
                args=((locations, i, seed_pair)),
            )
            p.start()
            processes.append(p)

        for p in processes:
            p.join()

        print("All processes finished running!")

        return min(locations)


if __name__ == "__main__":
    output = solve("./task_input/input.txt")
    print("Output", output)
