from mock_examples.api import get_weather


def test_get_weather_mocked(mocker):
    """
    Function to test get weather with mocked response
    """
    mock_data = {
        "temperature": "+7 °C",
        "wind": "13 km/h",
        "description": "Partly cloudy",
        "forecast": [
            {"day": "1", "temperature": "+10 °C", "wind": "13 km/h"},
            {"day": "2", "temperature": "+6 °C", "wind": "26 km/h"},
            {"day": "3", "temperature": "+15 °C", "wind": "21 km/h"},
        ],
    }

    # Create a mock response object with a .json() method that returns the mock data
    mock_response = mocker.MagicMock()
    mock_response.json.return_value = mock_data
    mock_response.status_code = 200  # Mocking status code as well

    # Patch 'requests.get' to return the mock response
    mocker.patch("requests.get", return_value=mock_response)

    # Call the function
    result = get_weather(city="London")

    # Assertions to check if the returned data is as expected
    assert result == mock_data
    assert mock_response.status_code == 200
    assert isinstance(result, dict)
    assert result["temperature"] == "+7 °C"
    assert result["wind"] == "13 km/h"
