import unittest
from unittest import TestCase
from unittest.mock import patch, Mock

from tests.mockings.prod.mathematics import Calculations


class TestMock1(TestCase):

    @patch("tests.mockings.prod.mathematics.Calculations.div_mod")
    def test_sum_the_divmod1(self, mock_div_mod):
        mock_div_mod.return_value = (2, 1)

        cal = Calculations()
        result = cal.div_mod(3, 2)

        assert result == (2, 1)

    @patch("tests.mockings.prod.mathematics.Calculations.summation")
    def test_sum_the_divmod2(self, mock_summation):
        mock_summation.return_value = 1

        cal = Calculations()
        result1 = cal.summation(2, 4)
        result2 = cal.summation(5, 3)

        assert result1 + result2 == 2

if __name__ == '__main__':
    unittest.main()