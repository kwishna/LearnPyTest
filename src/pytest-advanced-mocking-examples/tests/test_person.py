import pytest
from mock_examples.person import (
    Person,
)  


@pytest.fixture
def person_fixture(): 
    """
    Fixture to create a Person object.
    """
    person = Person(name="Eric", age=25, address="123 Farmville Rd")
    return person 


def test_person_properties(person_fixture):
    """
    Test individual properties of the Person class.
    """
    assert person_fixture.name == "Eric"
    assert person_fixture.age == 25
    assert person_fixture.address == "123 Farmville Rd"


def test_person_class_with_mock(mocker):
    """
    Test the Person class using a mock for the 'get_person_json' method
    """
    person = Person(name="Eric", age=25, address="123 Farmville Rd")
    mock_response = {"name": "FAKE_NAME", "age": "FAKE_AGE", "address": "FAKE_ADDRESS"}

    # Patch the method
    mocker.patch.object(person, "get_person_json", return_value=mock_response)

    assert person.get_person_json() == mock_response
