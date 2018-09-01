from packages.date_tools import Project
from packages.date_tools import Date
from packages.date_tools import Task
import os


class ProjectWriter(object):
    def __init__(self, project):
        self.file_name = project.get_name().lower().replace(" ", "_")
        self.file_obj = None
        self.input_project = project
        folder_name = "my_projects"  # folder name
        self.path = folder_name + "/" + self.file_name + ".txt"

        # create the folder if it's doesn't exist
        if not os.path.isdir(folder_name):
            os.makedirs(folder_name)

    def _print_record(self):
        self.file_obj.write(str(self.input_project))

    def open(self):
        self.file_obj = open(self.path, "w")

    def save_project(self):
        self._print_record()

    def close(self):
        self.file_obj.close()
