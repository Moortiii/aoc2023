def below_range(range1, range2):
    if range1.stop < range2.start:
        return range1

    if range1.start > range2.start:
        return range(0, 0)
    elif range1.start < range2.start and range2.start < range1.stop:
        return range(range1.start, range2.start)
    elif range1.start < range2.start and range2.start > range1.stop:
        return range(range1.start, range2.start)


def above_range(range1, range2):
    if range1.start > range2.stop:
        return range1

    if range1.start < range2.stop and range1.stop > range2.stop:
        return range(0, 0)

    if range1.start < range2.stop and range1.stop < range2.stop:
        return range(range1.st)


def test_below_range():
    assert below_range(range(40, 50), range(60, 100)) == range(40, 50)
    assert below_range(range(40, 60), range(60, 100)) == range(40, 60)
    assert below_range(range(40, 80), range(60, 100)) == range(40, 60)
    assert below_range(range(40, 110), range(60, 100)) == range(40, 60)
    assert below_range(range(80, 90), range(60, 100)) == range(0, 0)
    assert below_range(range(80, 110), range(60, 100)) == range(0, 0)
    assert below_range(range(140, 150), range(60, 100)) == range(0, 0)


def test_above_range():
    assert above_range(range(40, 50), range(60, 100)) == range(0, 0)
    assert above_range(range(50, 110), range(60, 100)) == range(100, 110)
    assert above_range(range(60, 100), range(60, 100)) == range(0, 0)
    assert above_range(range(100, 150), range(60, 100)) == range(100, 150)
    assert above_range(range(110, 120), range(60, 100)) == range(110, 120)
