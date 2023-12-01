from solver import utils

mapping = {
    "o": ["ne"],
    "t": ["wo", "hree"],
    "f": ["our", "ive"],
    "s": ["ix", "even"],
    "e": ["ight"],
    "n": ["ine"],
}

str_to_int = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def solve(input_file: str):
    lines = utils.read_lines(input_file)

    numbers = []

    for line in lines:
        digits = []

        for i, char in enumerate(line):
            if char.isdigit():
                digits.append(int(char))
                continue

            if char in "otfsen":
                for combination in mapping[char]:
                    for j, map_char in enumerate(combination):
                        if len(line) <= i + j + 1:
                            break

                        if line[i + j + 1] != map_char:
                            break
                    else:
                        digits.append(str_to_int[f"{char}{combination}"])

        numbers.append(int(f"{digits[0]}{digits[-1]}"))

    return sum(numbers)
