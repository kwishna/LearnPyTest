import pytest


@pytest.fixture(params=[1, 2, 3])
def number(request):
    return request.param


def test_even(number):
    assert number % 2 == 0
