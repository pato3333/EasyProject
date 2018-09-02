from packages.read_functions import name_to_path, is_file, project_record_to_project
from packages.store_tools import ProjectReader
from packages.date_tools import Project


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
        else:
            raise ValueError('The number or type of argument isn\'t correct')

    def get_project(self):
        return self.project
