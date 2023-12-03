from solver import utils


def test__read_lines_single_line(fs):
    fs.create_file("input.txt", contents="This is my content")
    assert utils.read_lines("input.txt") == ["This is my content"]


def test__read_lines_multiline(fs):
    fs.create_file(
        "input.txt",
        contents=(
            """
            The first line
            The second line
            """
        ).strip(),
    )
    assert utils.read_lines("input.txt") == ["The first line", "The second line"]


def test__read_numbers(fs):
    fs.create_file("input.txt", contents="1,2,3,4,5")
    assert utils.read_numbers("input.txt") == [1, 2, 3, 4, 5]
