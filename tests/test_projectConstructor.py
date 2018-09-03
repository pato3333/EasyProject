from unittest import TestCase
from packages.interface import ProjectConstructor


class TestProjectConstructor(TestCase):
    def test_get_project(self):
        cont = ProjectConstructor("Calendar Program")
        proj = cont.get_project()
        proj.set_name("Calendar Program 3.0")
        proj.save()
