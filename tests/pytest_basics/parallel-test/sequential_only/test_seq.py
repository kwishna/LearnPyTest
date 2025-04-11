import pytest

summation = 0

@pytest.mark.xdist_group(name="sequential_group")
def test_sequential_one():
    global summation
    summation += 1
    assert summation == 1

@pytest.mark.xdist_group(name="sequential_group")
def test_sequential_two():
    global summation
    summation += 1
    assert summation == 2

# All tests in sequential_group run se