import argparse
import os
import subprocess
from datetime import datetime

import requests
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    aoc_session: str = Field(..., validation_alias="AOC_SESSION")
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()

parser = argparse.ArgumentParser(
    prog="Advent of Code Generator",
    description="Generate template for solving Advent of Code problems",
    epilog="Happy solving!",
)

parser.add_argument(
    "-d",
    "--day",
    default=datetime.today().day,
    type=int,
    help="The day to generate a template for. Default: current date",
)
parser.add_argument(
    "-y",
    "--year",
    default=datetime.today().year,
    type=int,
    help="The year to generate a template for. Default: current year",
)

parser.add_argument(
    "-c",
    "--no-code",
    default=False,
    help="Run without starting VSCode. Default: false",
    action="store_true",
)

args = parser.parse_args()

selected_date = f"day{str(args.day).zfill(2)}"

if os.path.exists(f"{args.year}/{selected_date}"):
    print(f"Project for {selected_date} already exists, not overwriting")
else:
    os.makedirs(f"{args.year}", exist_ok=True)
    subprocess.run(f"cp -r ./template {args.year}/{selected_date}", shell=True)
    subprocess.run(
        f"rm -rf ./{args.year}/{selected_date}/tests/test_utils.py", shell=True
    )

session = requests.Session()
session.cookies.set("session", settings.aoc_session)

# If the puzzle input request failed, we can simply retry the command
puzzle_input = session.get(
    f"https://adventofcode.com/{args.year}/day/{args.day}/input",
).text[:-1]

with open(f"{args.year}/{selected_date}/task_input/input.txt", "w+") as f:
    f.write(puzzle_input)

if not args.no_code:
    subprocess.run(
        (
            f"code ./{args.year}/{selected_date} "
            f"./{args.year}/{selected_date}/task_input/test_1.txt "
            f"./{args.year}/{selected_date}/tests/test_solve.py "
            f"./{args.year}/{selected_date}/solver/part_1.py "
            f"./{args.year}/{selected_date}/solver/part_2.py"
        ),
        shell=True,
    )

subprocess.run(
    f"cd {args.year}/{selected_date} && poetry install && ./run.sh", shell=True
)
