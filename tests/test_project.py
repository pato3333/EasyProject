from unittest import TestCase
from packages.date_tools import Project
from packages.date_tools import Date
from packages.date_tools import Task


class TestProject(TestCase):

    def setUp(self):
        self.new_proj = Project(Date(9, 1, 2018), Date(9, 12, 2018), "Calendar Program")

    def test_project_method(self):
        task1 = Task(Date(9, 3, 2018), "Fix readme", "The readme needs to be complete")
        self.new_proj.add_task(task1)
        task2 = Task(Date(10, 3, 2018), "Implement user-interface", "The program needs to get data from the user")
        self.new_proj.add_task(task2)
        self.new_proj.remove_task(task1)
        self.new_proj.remove_task(task2)

        # self.new_proj.print_task_all()
        # print(self.new_proj)

        self.assertEqual(0, len(self.new_proj))
