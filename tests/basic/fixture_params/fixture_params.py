''' In this example, we make use of pytest framework along with Selenium '''
import pytest
from time import sleep
from contextlib import contextmanager

@pytest.fixture(params=["chrome", "firefox"], scope="class")
def browser(request):
    print("--- start ---")
    yield request.param
    print("--- end ---")

def test_browser(browser):
    assert browser.title is not None


# @pytest.mark.usefixtures("browser_name")
@pytest.mark.parametrize("browser_name", ["chromium", "gecko"])
def test_example(browser, browser_name):
    print(f'---- {browser} ----')
    print(f'---- {browser_name} ----')
    assert browser is not None
