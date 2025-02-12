import unittest
from unittest import TestCase, mock
from unittest.mock import patch, Mock

from tests.mockings.prod import get_cars


def my_function():
    return "Real Value"

class TestMock(TestCase):
    @patch("tests.mockings.prod.get_cars")
    def test_mocked_function(self, mocked_func):
        mocked_val = ['mocked_car1', 'mocked_car2']
        mocked_func.return_value = mocked_val
        self.assertEqual(mocked_func(), mocked_val)

    def test_mocked_function2(self):
        with patch("tests.mockings.prod.get_cars") as mock_get_cars:
            mock_get_cars.return_value = ['cycle']
            assert mock_get_cars() == ['cycle']

    def test_mocked_function3(self):
        with patch("tests.mockings.prod.get_cars", return_value=['cycle']) as mock_get_cars:
           assert mock_get_cars() == ['cycle']

    @patch("tests.mockings.patching_001.my_function")
    def test_mock_module_method(self, mock_function):
        mock_function.return_value = ['cycle']
        data = my_function()
        self.assertEqual(data, ['cycle'])

if __name__ == '__main__':
    unittest.main()