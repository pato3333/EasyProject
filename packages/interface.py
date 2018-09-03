from packages.read_functions import name_to_path, is_file, project_record_to_project
from packages.store_tools import ProjectReader
from packages.date_tools import Project, Task, Bag
from packages.read_functions import string_to_date


class TaskConstructor(object):
    def __init__(self):
        print("When do you want to do this task?:")
        self.date = input("> ")
        print("Choose a name:")
        self.title = input("> ")
        print("Write a brief description of this task:")
        self.description = input("> ")
        self.task = Task(string_to_date(self.date), self.title.strip().upper(), self.description.strip())

    def get_task(self):
        return self.task


class TaskBagConstructor(object):
    def __init__(self):
        scape_sequence = "n"
        self.task_bag = Bag()

        while scape_sequence == "n":
            print("Write the tasks who need to do to achieve your aim:")
            task_c = TaskConstructor()
            self.task_bag.add(task_c.get_task())
            print("Do you want to add one more task? (Answer= y/n)")
            scape_sequence = input("> ")

    def get_bag(self):
        return self.task_bag


class ProjectConstructor(object):
    def __init__(self, name, from_date=None, to_date=None):
        if from_date is None and to_date is None:
            path = name_to_path(name)
            if is_file(path):
                reader = ProjectReader(path)
                reader.open()
                self.project = project_record_to_project(reader.read())
                reader.close()
            else:
                raise ValueError('path is not correct')
        elif from_date is not None and to_date is not None:
            self.project = Project(from_date, to_date, name)
            self._set_tasks()
        else:
            raise ValueError('The number or type of argument isn\'t correct')

    def set_description(self, description):
        print("What do you achieve with this project?")
        description = input("> ")
        self.project.set_description(description)

    def _set_tasks(self):
        task_c = TaskBagConstructor()
        self.project.set_tasks(task_c.get_bag())

    def save_project(self):
        self.save_project()

    def add_task(self):
        task_co = TaskConstructor()
        self.project.add_task(task_co.get_task())

    def get_project(self):
        return self.project
