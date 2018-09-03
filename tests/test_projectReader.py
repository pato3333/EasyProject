from unittest import TestCase
from packages.store_tools import *
from packages.date_tools import *


class TestProjectReader(TestCase):
    def test_read(self):
        self.new_proj = Project(Date(9, 1, 2018), Date(9, 12, 2018), "Calendar Program")
        self.new_proj.set_description("This is the description.")
        task1 = Task(Date(9, 3, 2018), "Fix readme", "The readme needs to be complete")
        self.new_proj.add_task(task1)
        task2 = Task(Date(10, 3, 2018), "Implement user-interface", "The program needs to get data from the user")
        self.new_proj.add_task(task2)
        writer = ProjectWriter(self.new_proj)
        writer.open()
        writer.save_project()
        writer.close()
        path = writer.get_path()
        reader = ProjectReader(path)
        records = ProjectRecord()
        reader.open()
        records = reader.read()
        reader.close()

        self.assertEqual(records.name, "CALENDAR PROGRAM")
        self.assertEqual(records.to_date, "09/12/2018")
        self.assertEqual(2, len(records.tasks))
