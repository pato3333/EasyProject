from unittest import TestCase
from packages.date_tools import Bag


class TestBag(TestCase):
    def test_add(self):
        b1 = Bag()
        b1.add("Hello")
        b1.add("World")
        self.assertEqual(2, len(b1))
        self.assertTrue("Hello" in b1)

    def test_remove(self):
        b1 = Bag()
        b1.add("Hello")
        b1.add("World")
        b1.remove("Hello")
        self.assertFalse("Hello" in b1)
        self.assertTrue("World" in b1)
        self.assertEqual(1, len(b1))
