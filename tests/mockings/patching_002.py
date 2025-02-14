import unittest
from unittest import TestCase
from unittest.mock import patch

from tests.mockings.prod import ProductionDB

class TestMock(TestCase):
    @patch("tests.mockings.prod.ProductionDB.admin", False)
    def test_mocked_attribute(self):
        assert ProductionDB.admin == False, f"Should be {ProductionDB.admin}"

    @patch("tests.mockings.prod.ProductionDB.get_car_price")
    def test_mocked_function(self, mock_get_car_price):
        mock_get_car_price.return_value = 1

        db = ProductionDB()
        assert db.get_car_price("audi") == 1


if __name__ == '__main__':
    unittest.main()