import unittest
from unittest import TestCase
from unittest.mock import Mock, MagicMock

class TestMock(TestCase):
    def test_simple_mock(self):
        my_mock = Mock()
        my_mock.return_value = "mocked"

        result = my_mock()
        self.assertEqual(result, "mocked")

if __name__ == '__main__':
    unittest.main()