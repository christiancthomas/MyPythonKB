"""
Unit test for the income_calculator.py
"""
import unittest

from income_calculator import calculate_net_monthly_income, calculate_yearly_income


class TestIncomeCalculations(unittest.TestCase):
    """
    Test cases for income calculation functions.
    """

    def test_calculate_net_monthly_income(self):
        """
        Test the net monthly income calculation.
        """
        self.assertEqual(calculate_net_monthly_income(5000, 1000), 4000)
        self.assertEqual(calculate_net_monthly_income(3000, 500), 2500)
        self.assertEqual(calculate_net_monthly_income(7000, 2000), 5000)

    def test_calculate_yearly_income(self):
        """
        Test the yearly income calculation.
        """
        self.assertEqual(calculate_yearly_income(4000), 48000)
        self.assertEqual(calculate_yearly_income(2500), 30000)
        self.assertEqual(calculate_yearly_income(5000), 60000)


if __name__ == "__main__":
    unittest.main()
