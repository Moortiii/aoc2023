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

args = parser.parse_args()

selected_date = f"day{str(args.day).zfill(2)}"

if os.path.exists(selected_date):
    print(f"Project for {selected_date} already exists, not overwriting")
else:
    subprocess.run(f"cp -r ./template {selected_date}", shell=True)

session = requests.Session()
session.cookies.set("session", settings.aoc_session)

# If the puzzle input request failed, we can simply retry the command
puzzle_input = session.get(
    f"https://adventofcode.com/2023/day/{args.day}/input",
).text[:-1]

with open(f"{selected_date}/task_input/input.txt", "w+") as f:
    f.write(puzzle_input)

subprocess.run(
    (
        f"code ./{selected_date} "
        f"./{selected_date}/task_input/test_1.txt "
        f"./{selected_date}/tests/test_solve.py "
        f"./{selected_date}/solver/part_1.py"
    ),
    shell=True,
)

subprocess.run(f" cd {selected_date} && poetry install && ./run.sh", shell=True)
