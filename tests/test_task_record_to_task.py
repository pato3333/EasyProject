from unittest import TestCase
from packages.read_functions import *
from packages.date_tools import Date, Task
from packages.store_tools import TaskRecord


class Test_task_record_to_task(TestCase):
    def test_task_record_to_task(self):
        tr = TaskRecord()
        tr.name = "HOLA"
        tr.date = "09/13/2018"
        tr.notes = "there are the notes"
        tr.status = "To Do"

        t = Task(Date(9, 13, 2018), "Hola", "there are the notes")

        self.assertEqual(t, task_record_to_task(tr))

        # get's function not equal to self...
