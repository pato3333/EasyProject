from packages.date_tools import *


def string_to_date(string):
    """
    Convert a string into a date data type.
    :param string: ##/##/####
    :return: date data type
    """
    assert len(string) == 10, "Not valid value"
    date_list = string.split("/")
    return Date(int(date_list[0]), int(date_list[1]), int(date_list[2]))


def task_record_to_task(taskRecord):
    """
    Convert a taskRecord data type into a task data type
    :param taskRecord
    :return: task data type
    """
    return Task(string_to_date(taskRecord.date), taskRecord.name, taskRecord.notes)


def task_record_list_to_task_bag(task_record_list):
    """
    Convert a taskRecord list into a task Bag
    :param task_record_list
    :return: task bag
    """
    re_bag = Bag()
    for x in task_record_list:
        re_bag.add(task_record_to_task(x))

    return re_bag


def project_record_to_project(project_record):
    """
    Convert a projectRecord data type into project data type
    :param project_record:
    :return:
    """
    pro_from_date = string_to_date(project_record.from_date)
    pro_to_date = string_to_date(project_record.to_date)
    pro_name = project_record.name
    pro_description = project_record.description
    pro_tasks = task_record_list_to_task_bag(project_record.tasks)

    re_pro = Project(pro_from_date, pro_to_date, pro_name)
    re_pro.set_tasks(pro_tasks)
    re_pro.set_description(pro_description)

    return re_pro
