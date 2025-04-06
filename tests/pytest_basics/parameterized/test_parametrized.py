import pytest, re

def is_palindrome(string):
    # Normalize the string: convert to lowercase and remove non-alphanumeric characters
    normalized_string = re.sub(r'[^a-zA-Z0-9]', '', string).lower()

    # Check if the normalized string is equal to its reverse
    return normalized_string == normalized_string[::-1]

@pytest.mark.parametrize("maybe_palindrome, expected_result", [
    ("", True),
    ("a", True),
    ("Bob", True),
    ("Never odd or even", True),
    ("Do geese see God?", True),
    ("abc", False),
    ("abab", False),
])

@pytest.mark.param
def test_is_palindrome(maybe_palindrome, expected_result):
    assert is_palindrome(maybe_palindrome) == expected_result

