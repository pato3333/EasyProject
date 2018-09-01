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
        return "%02i/%02i/%04i\n" % (self._month, self._day, self._year)

    def __eq__(self, other):
        return other.to_julian_day() == self.to_julian_day()

    def print_julian(self):
        return self.to_julian_day()

    def __gt__(self, other):
        return self.to_julian_day() > other.to_julian_day()


class Task(object):
    def __init__(self, date, title, notes):
        self.input_date = date
        self.input_title = title
        self.input_notes = notes


class Project(object):
    def __init__(self, from_date, to_day, name):
        assert from_date < to_day, "The dates are not valid"

        self.from_date = from_date
        self.to_date = to_day
        self.name = name
        self.description = None

    def set_description(self, string):
        self.description = string

    def set_name(self, new_name):
        self.name = new_name

