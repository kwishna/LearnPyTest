import pytest

@pytest.mark.order(2)
def test_foo():
    assert True

@pytest.mark.order(1)
def test_bar():
    assert True

"""
Use pytest-order only for tests within the same file when running with pytest-xdist.
Run pytest with --dist=loadfile to keep tests from the same file on the same worker.

pytest -n auto --dist=loadfile
"""