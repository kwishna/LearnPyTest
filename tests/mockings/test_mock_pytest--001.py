from unittest.mock import MagicMock

import pytest


class ProductionDB:
    def get_car_price(self, name):
        PRICES = {
            'buggatti': 1000,
            'audi': 500,
            'maruti': 100,
        }
        return PRICES[name]

class TestDB:
    # @pytest.mark.mock1
    def test_car_price(self):
        db = ProductionDB()
        db.get_car_price = MagicMock(return_value=3)
        # db.method('audi', key='value')
        # db.method.assert_called_with(3, 4, 5, key='value')
        assert db.get_car_price('audi') == 3