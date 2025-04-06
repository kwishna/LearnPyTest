import pytest
import logging

@pytest.mark.no_cover
def test_always_passes(*args, **kwargs):
    logging.info(f"---- test_always_passes ----")
    logging.info(f"{args}")
    logging.info(f"{kwargs}")
    assert True

@pytest.mark.no_cover
def test_always_fails():
    logging.info(f"---- test_always_passes ----")
    assert False