from unittest import TestCase
from packages.date_tools import is_year_leap


class TestIs_year_leap(TestCase):
    def test_is_year_leap(self):
        self.assertTrue(is_year_leap(2012))
        self.assertFalse(is_year_leap(2011))


