import pytest
import asyncio
import pytest_asyncio


# Async fixtures
@pytest_asyncio.fixture
async def loaded_data():
    await asyncio.sleep(1)  # Simulate loading data asynchronously
    return {"key": "value"}


# Async test functions with fixtures
@pytest.mark.asyncio
async def test_fetch_data(loaded_data):
    print(f'--- {loaded_data} ---')
    assert loaded_data["key"] == "value"
