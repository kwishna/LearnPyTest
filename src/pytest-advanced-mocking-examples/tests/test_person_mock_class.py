import pytest
from mock_examples import person


@pytest.fixture
def mock_person_class(mocker):
    """
    Fixture to mock the entire Person class.
    """
    return mocker.patch(
        "mock_examples.person.Person", autospec=True
    )  # autospec=True ensures that the mock has the same interface as the class being mocked


def test_person_class_is_mocked(mock_person_class):
    """
    Test to verify that the Person class is mocked.
    """
    mock_person_instance = (
        mock_person_class.return_value
    )  # `mock_person_class.return_value` is the mock object that simulates any instance of 'Person'
    mock_person_instance.get_person_json.return_value = (
        {  # You set up what the `get_person_json` method should return when called
            "name": "FAKE_NAME",
            "age": "FAKE_AGE",
            "address": "FAKE_ADDRESS",
        }
    )

    # When you create a 'Person', you're using the mock, not the real Person class
    eric = person.Person("Eric", 25, "123 Farmville Rd")
    result = eric.get_person_json()  # # This calls the mocked method

    # Assert that the mocked method returns what you expect
    assert result == {
        "name": "FAKE_NAME",
        "age": "FAKE_AGE",
        "address": "FAKE_ADDRESS",
    }

    # Assert that the Person was instantiated correctly in the mock
    mock_person_class.assert_called_once_with("Eric", 25, "123 Farmville Rd")

    # Assert that the method was called on the mock instance
    mock_person_instance.get_person_json.assert_called_once()
