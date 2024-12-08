import pytest

@pytest.mark.no_cover
def test_always_passes():
    assert True

@pytest.mark.no_cover
def test_always_fails():
    assert False