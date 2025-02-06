from unittest import TestCase
import unittest
from unittest.mock import MagicMock

from tests.mockings.prod import ProductionDB


class TestMagicMock(TestCase):
    def test_magic_mock(self):
        my_mock = MagicMock(spec=ProductionDB)

        my_mock.get_car_price.return_value = 5
        price = my_mock.get_car_price('audi')
        assert price == 5



if __name__ == '__main__':
    unittest.main()