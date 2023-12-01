# Advent of Code 2023

    ||::|:||   .--------,
    |:||:|:|   |_______ /        .-.
    ||::|:|| ."`  ___  `".    {\('v')/}
    \\\/\///:  .'`   `'.  ;____`(   )'____
     \====/ './  o   o  \|~     ^" "^   //
      \\//   |   ())) .  |   Season's    \
       ||     \ `.__.'  /|   Greetings  //
       ||   _{``-.___.-'\|              \
       || _." `-.____.-'`|    ___       //
       ||`        __ \   |___/   \_______\
     ."||        (__) \    \|     /
    /   `\/       __   vvvvv'\___/
    |     |      (__)        |
     \___/\                 /
       ||  |     .___.     |
       ||  |       |       |
       ||.-'       |       '-.
       ||          |          )
       ||----------'---------'

Art copied from: https://saravitaya.tripod.com/_ArtXmas.html

## Using the template

Install the dependencies:

    poetry install

Log into Advent of Code on the Website and fetch your session cookie. Place the value in a file named `.env` at the top level with the contents:

    AOC_SESSION=<session-cookie-value-here>

The setup above only needs to be carried out once.

Create a new project for the current day:
    
    poetry run python setup.py
    
Create a new project for an arbitrary day:

    poetry run python setup.py -d 12

Defaults to the current day unless specified.

## What does the template achieve?

Behind the scenes the script does the following:

1. Copies the template to the selected date.
   
   We use the config option `poetry config virtualenvs.in-project true --local` to ensure the environment is local and can be updated with new dependencies on demand when working on a given task.

2. Fetches the puzzle input for the selected day and places it into `input.txt` in the task_input folder
3. Opens an editor with the example input, tests file and python file for part 1 open. This allows us to quickly copy the minimal example from the website, modify the expected value in the test with the value shown on the website, and start solving the problem
4. Starts a file watcher on the current directory, both for .txt and .py files. Whenever a file changes, the terminal will be cleared and pytest will re-run
5. Checks if the solver functions return an output, to prevent cluttering the test output. Unless a value is explicitly returned, the test is skipped

The program checks if the current day exists before modifying files on the system. As a result, re-running the command is always safe.

## About run.sh

There are a lot of options present in `run.sh` that probably warrant an explanation, and that I'll thank myself for having documented when I repeat this next year.

The flag `PYTHONDONTWRITEBYTECODE=1` prevents Python from writing `__pycache__` directories during runs, which create a lot of visual clutter. The scripts are so small that the overhead of running without cache doesn't matter.

The following options are passed to `pytest-watch`:

    -c: Clear the terminal between each run of Pytest issued by `pytest-watch`

    --ext: Watch only for changes in files with this extension

    --ignore: Ignore the following directories when watching for changes, regardless of extension

The following options are passed along from `pytest-watch` directly to `pytest`:

    -raFP: Print an aggregated test report with failed and passed tests at the end. This ensures the output for the tests is always located at the bottom, regardless of how many prints you issue in the solver code.

    -W ignore::pytest.PytestReturnNotNoneWarning: We issue an early return if one of the solvers returns `None` in order to prevent the tests from running until we have started working on a solution. This prevents Pytest from issuing a warning about this.

    -p no:cacheprovider: Prevents pytest from writing .pytest_cache directories during runs
