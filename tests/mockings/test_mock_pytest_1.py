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

    @pytest.mark.mock2
    def test_car_price2(self):
        db = ProductionDB()
        db.method = MagicMock()
        db.method(3, 4, 5, key='value')
        db.method.assert_called_with(3, 4, 5, key='value')

    @mock.patch("requests.get")
    def test_mock_module_method(self, mock_req):
        mock_resp = Mock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = { "id": 1 }

        mock_req.return_value = mock_resp

        data = requests.get("https://localhost")
        assert data.status_code == 200
        assert data.json() == { "id": 1 }