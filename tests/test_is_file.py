from unittest import TestCase
from packages.read_functions import is_file


class TestIs_file(TestCase):
    def test_is_file(self):
        self.assertTrue(is_file("my_projects/calendar_program.txt"))
        self.assertFalse(is_file("my_project/hola.txt"))
        self.assertTrue(is_file("my_projects/calendar_program_2.0.txt"))
