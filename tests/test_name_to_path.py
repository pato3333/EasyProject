from unittest import TestCase
from packages.read_functions import name_to_path


class TestName_to_path(TestCase):
    def test_name_to_path(self):
        self.assertEqual("my_projects/hola_mundo.txt", name_to_path("HolA Mundo"))
