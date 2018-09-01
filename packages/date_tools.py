def is_year_leap(year):
    if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
        return True
    else:
        return False


def days_of_month(month, year):
    d31 = [1, 3, 5, 7, 8, 10, 12]
    d30 = [4, 6, 9, 11]
    if month in d31:
        return 31
    elif month in d30:
        return 30
    else:
        if is_year_leap(year):
            return 29
        else:
            return 28


def _is_valid_date(m, d, y):
    if m > 0 and y > 0 and d > 0:
        if m <= 12:
            if d <= days_of_month(m, y):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


class Date(object):
    def __init__(self, m, d, y):
        assert _is_valid_date(m, d, y), "Not valid date input"

        self._day = d
        self._month = m
        self._year = y

    def to_julian_day(self):
        t = 0  # python do wrong this operation -11/12
        if self._month < 3:
            t = -1

        j_day = (1461 * (self._year + 4800 + t)) // 4 \
                 + (367 * (self._month - 2 - 12 * t)) // 12 \
                 - (3 * ((self._year + 4900 + t) // 100)) // 4 \
                 + self._day - 32075

        return j_day

    def __sub__(self, other):
        return self.to_julian_day() - other.to_julian_day()

    def month_name(self):
        name = ["June", "February", "Mars", "April", "May", "June", "July", "August"
            , "September", "October", "November", "December"]
        return name[self._month - 1]

    def day_number_week(self):
        return (self.to_julian_day() + 1) % 7

    def day_name(self):
        name = ["Sun", "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat"]
        return name[self.day_number_week()]

    def __str__(self):
        return "%02i/%02i/%04i" % (self._month, self._day, self._year)

    def __eq__(self, other):
        return other.to_julian_day() == self.to_julian_day()

    def print_julian(self):
        return self.to_julian_day()

    def __gt__(self, other):
        return self.to_julian_day() > other.to_julian_day()


def _date_task(task):
    """
    Return the date of the task
    :param task
    :return: the date of the task
    """
    return task.date


class Task(object):
    def __init__(self, date, title, notes):
        assert len(notes) < 60, "You can't write more than 60 character"
        self.input_date = date
        self.input_title = title.upper()
        self.input_notes = notes

    def __str__(self):
        record = "%s\n%s\n" % (self.input_title, self.input_date)
        description = "%s\n" % self.input_notes
        return ".\n" + record + description

    def title(self):
        return self.input_title

    def date(self):
        return self.input_date

    def notes(self):
        return self.input_notes

    def __eq__(self, other):
        return self.input_title == other.input_title and self.input_date == other.input_date \
               and self.input_notes == other.input_notes


class _BagIterator(object):
    def __init__(self, container):
        self.container = container
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < len(self.container):
            item = self.container[self.current_index]
            self.current_index += 1
            return item
        else:
            raise StopIteration


class Bag(object):
    def __init__(self):
        self.container = list()

    def add(self, item):
        self.container.append(item)

    def __len__(self):
        return len(self.container)

    def __contains__(self, item):
        return item in self.container

    def remove(self, item):
        assert item in self.container, "The item must be in the bag"
        ind = self.container.index(item)
        return self.container.pop(ind)

    def __iter__(self):
        return _BagIterator(self.container)


class Project(object):
    def __init__(self, from_date, to_day, name):
        assert from_date < to_day, "The dates are not valid"

        self.from_date = from_date
        self.to_date = to_day
        self.name = name.upper()
        self.description = ""
        self.tasks = Bag()

    def set_description(self, string):
        self.description = string

    def set_name(self, new_name):
        self.name = new_name

    def add_task(self, new_task):
        self.tasks.add(new_task)

    def __len__(self):
        return len(self.tasks)

    def __str__(self):
        title = self.name + "\n"
        note = self.description + "\n"
        to_d = str(self.to_date) + "\n"
        from_d = str(self.from_date) + "\n"

        if self.__len__() == 0:
            task = "None"
        else:
            task = self.print_task_all()
        return title + note + to_d + from_d + task

    def remove_task(self, task):
        self.tasks.remove(task)

    def print_task_all(self):
        str_task = ""
        for x in self.tasks:
            str_task += str(x)
        return str_task

    def _get_task_for_title(self, title):
        real_title = title.upper()
        for x in self.tasks:
            if x.title() == real_title:
                return x
            else:
                return None

    def is_task(self, title):
        """
        Verified that the task with title: title is in the project
        :param title: title of the task
        :return: True is the task with name Title is in the project, False if it isn't
        """
        task = self._get_task_for_title(title)
        if task in self.tasks:
            return True
        else:
            return False

    def get_name(self):
        return self.name

    def set_tasks(self, task_bag):
        self.tasks = task_bag
