from unittest import TestCase
from packages.date_tools import Date


class TestDate(TestCase):

    def setUp(self):
        self.d1 = Date(8, 31, 2018)
        self.d2 = Date(9, 3, 2018)
        self.d3 = Date(2, 29, 2012)

    def test_print_julian(self):
        self.assertEqual(2458362, self.d1.print_julian())
        self.assertEqual(2458365, self.d2.print_julian())
        self.assertEqual(2455987, self.d3.print_julian())

    def test_dif_day(self):
        self.assertEqual(3, self.d2 - self.d1)

    def test_month_name(self):
        self.assertEqual("August", self.d1.month_name())
        self.assertEqual("September", self.d2.month_name())

    def test_day_number_week(self):
        self.assertEqual(5, self.d1.day_number_week())
        self.assertEqual(1, self.d2.day_number_week())
        self.assertEqual(3, self.d3.day_number_week())

    def test_day_name(self):
        self.assertEqual("Fri", self.d1.day_name())
        self.assertEqual("Mon", self.d2.day_name())
        self.assertEqual("Wed", self.d3.day_name())
