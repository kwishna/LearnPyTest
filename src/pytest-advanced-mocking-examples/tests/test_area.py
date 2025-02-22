from mock_examples import area


def test_area_of_circle():
    """
    Function to test area of circle
    """
    assert area.area_of_circle(5) == 78.53975


def test_area_of_circle_with_mock(mocker):
    """
    Function to test area of circle with mocked PI value
    """
    mocker.patch("mock_examples.area.PI", 3.0)
    assert area.area_of_circle(5) == 75.0


def test_area_of_circle_mocked_function(mocker):
    """
    Function to test area of circle with mocked function
    """
    mocker.patch("mock_examples.area.area_of_circle", return_value=100)
    assert area.area_of_circle(5) == 100
