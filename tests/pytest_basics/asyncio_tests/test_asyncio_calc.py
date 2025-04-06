import pytest
import asyncio
import pytest_asyncio

class AsyncioCalImpl:

    @staticmethod
    async def async_add(a, b):
        print("Starting async_add")
        await asyncio.sleep(5)  # Simulate an async operation
        print("Result From async_add", a + b)
        return a + b

    @staticmethod
    async def async_sub(a, b):
        print("Starting async_sub")
        print("Result From async_sub", a - b)
        return a - b


async def main():
    # Schedule both async_add and async_sub to run concurrently.
    res_add, res_b = await asyncio.gather(
        AsyncioCalImpl.async_add(1, 2),  # Pass the first function call
        AsyncioCalImpl.async_sub(1, 2),  # Pass the second function call
    )
    print(res_add)
    print(res_b)


# Basic Async test function
@pytest.mark.asyncio
async def test_async_add():
    result = await AsyncioCalImpl.async_add(1, 2)
    assert result == 3


@pytest.mark.asyncio
async def test_async_sub():
    result = await AsyncioCalImpl.async_sub(1, 2)
    assert result == -1


# Async fixtures
@pytest_asyncio.fixture
async def loaded_data():
    await asyncio.sleep(1)  # Simulate loading data asynchronously
    return {"key": "value"}


# Async test functions with fixtures
@pytest.mark.asyncio
async def test_fetch_data(loaded_data):
    assert loaded_data["key"] == "value"