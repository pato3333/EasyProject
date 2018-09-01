from unittest import TestCase
from packages.read_functions import string_to_date
from packages.date_tools import Date


class TestString_to_date(TestCase):
    def test_string_to_date(self):
        string_date = "08/12/2018"
        date1 = Date(8, 12, 2018)
        self.assertEqual(string_to_date(string_date), date1)
