import pytest
import pytest_asyncio
from asyncmock import AsyncMock

import logging
import aiohttp


class CatFact:
    def __init__(self):
        self.base_url = "https://meowfacts.herokuapp.com/"

    async def get_cat_fact(self):
        """
        Asynchronously get a Cat Fact from Rest API and return a dict with status and fact.
        """
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.base_url) as response:
                    if response.status in (200, 201):
                        json_response = await response.json()
                        return {"status": response.status, "result": json_response}
                    else:
                        return {
                            "status": response.status,
                            "error": "Cat Fact Not Available",
                        }
        except aiohttp.ClientError as err:
            logging.error(f"Client error: {err}")
            return {"status": 500, "error": "Failed to fetch Cat Fact"}
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            return {"status": 500, "error": "Failed to fetch Cat Fact"}


# async def main():
#     cat_fact = CatFact()
#     result = await cat_fact.get_cat_fact()
#     print(result)
#
#
# if __name__ == "__main__":
#     asyncio.run(main())


@pytest_asyncio.fixture
async def cat_fact():
    return CatFact()


# Test with Real API call (Not Recommended)
@pytest.mark.asyncio
async def test_get_cat_fact(cat_fact):
    result = await cat_fact.get_cat_fact()
    print(result)
    assert result["status"] == 200
    assert "data" in result["result"]


# Test with Mocked API call (Recommended when interacting with external services)
@pytest.mark.asyncio
async def test_get_cat_fact_mocked(mocker):
    # Mock the get_cat_fact method of CatFact
    mock_response = {"status": 200, "result": {"data": "Cats are awesome!"}}
    mocker.patch.object(CatFact, "get_cat_fact", AsyncMock(return_value=mock_response))

    cat_fact_instance = CatFact()
    result = await cat_fact_instance.get_cat_fact()

    assert result["status"] == 200
    assert "data" in result["result"]
    assert result["result"]["data"] == "Cats are awesome!"