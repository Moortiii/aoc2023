from solver import solve_1, solve_2


def test_part_1():
    output = solve_1("./task_input/test_1.txt")

    if output is None:
        return False

    assert output == 374

    output_1 = solve_1("./task_input/input.txt")
    print("\nPart 1 solution:", output_1)


def test_part_2():
    output = solve_2("./task_input/test_2.txt", expansion_factor=10)
    assert output == 1030

    output = solve_2("./task_input/test_2.txt", expansion_factor=100)
    assert output == 8410

    output_2 = solve_2("./task_input/input.txt", expansion_factor=1_000_000)
    print("\nPart 2 solution:", output_2)
