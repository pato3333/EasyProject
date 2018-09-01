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

    def get_path(self):
        return self.path


class ProjectRecord(object):
    def __init__(self):
        self.name = None
        self.description = None
        self.from_date = None
        self.to_date = None
        self.tasks = None


class TaskRecord(object):
    def __init__(self):
        self.name = None
        self.notes = None
        self.date = None


class ProjectReader(object):
    def __init__(self, path):
        assert os.path.isfile(path), "No file"
        self.file_path = path
        self.file_ob = None

    def _read_task(self):
        my_tasks = list()
        my_line = self.file_ob.readline().strip()
        while True:
            if my_line == ".":
                task_ins = TaskRecord()
                task_ins.name = self.file_ob.readline().strip()
                task_ins.date = self.file_ob.readline().strip()
                task_ins.notes = self.file_ob.readline().strip()
                my_tasks.append(task_ins)
                my_line = self.file_ob.readline().strip()
            else:
                break
        return my_tasks

    def open(self):
        self.file_ob = open(self.file_path, 'r')

    def read(self):
        out_pro = ProjectRecord()
        out_pro.name = self.file_ob.readline().strip()
        out_pro.description = self.file_ob.readline().strip()
        out_pro.from_date = self.file_ob.readline().strip()
        out_pro.to_date = self.file_ob.readline().strip()
        out_pro.tasks = self._read_task()

    def close(self):
        self.file_ob.close()
