from calc import total


def test_total_empty() -> None:
    # total of empty list should be 0.0
    assert total([]) == 0.0


def test_total_single_item() -> None:
    # total of list with a single item
    # should be just the first item
    assert total([110.0]) == 110.0


def test_total_multiple_item() -> None:
    # total of list with a multiple items
    # should be their sum
    assert total([1.0, 2.0, 3.0]) == 6.0
