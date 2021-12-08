from typing import NamedTuple, List
import pytest
from calc import total


class Case(NamedTuple):
    xs: List[float]
    expected: float


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


@pytest.mark.parametrize(
    ('xs', 'expected'),
    (
        ([], 0.0),
        pytest.param([110.0], 110.0),
        pytest.param([110.0], 110.0, id='single_item'),
        Case(xs=[1.0, 2.0, 3.0], expected=6.0)  # can't be simply passed into pytest.param()
    )
)
def test_total(xs, expected) -> None:
    assert total(xs) == expected
