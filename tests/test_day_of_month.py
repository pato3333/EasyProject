from unittest import TestCase
from packages.date_tools import days_of_month

class TestDay_of_month(TestCase):
    def test_days_of_month(self):
        self.assertEqual(31, days_of_month(8, 2018))
        self.assertEqual(28, days_of_month(2, 2018))
        self.assertEqual(30, days_of_month(9, 2018))
