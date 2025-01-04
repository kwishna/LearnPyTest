from unittest.mock import MagicMock, Mock
from unittest import mock

import pytest
import requests

from tests.mockings.prod import ProductionDB

class TestDB:
    @pytest.mark.mock1
    def test_car_price1(self):
        db = ProductionDB()
        db.get_car_price = MagicMock(return_value=3)
        assert db.get_car_price('audi') == 3

