import pytest
from dao import Dao


# https://docs.pytest.org/en/6.2.x/fixture.html#scope-sharing-fixtures-across-classes-modules-packages-or-session
@pytest.fixture(scope="module")
def dao_connection():
    print('setting up dao')
    return Dao()  # put a breakpoint to see that it only runs once


# https://docs.pytest.org/en/6.2.x/fixture.html#teardown-cleanup-aka-fixture-finalization
# @pytest.fixture(scope="module")
# def dao_connection():
#     print('setting up dao')
#     yield Dao()
#     print('cleaning up dao')


def test_get_all(dao_connection):
    assert dao_connection.get_all() == [1, 2, 3, 4, 5]


def test_get_first(dao_connection):
    assert dao_connection.get_first() == [1]
