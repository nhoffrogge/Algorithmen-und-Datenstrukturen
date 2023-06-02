from time import localtime

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __repr__(self):
        return f'{self.day}.{self.month}.{self.year}'

    def print_date(self):
        print(self)

    @classmethod
    def get_todays_date(cls):
        print(hex(id(cls)))
        date = cls.__new__(cls)
        print(hex(id(date)))
        time = localtime()
        date.year = time.tm_year
        date.month = time.tm_mon
        date.day =  time.tm_mday
        return date

    @staticmethod
    def is_todays_date(date):
        time = localtime()
        if (
            date.year == time.tm_year
            and date.month == time.tm_mon
            and date.day == time.tm_mday
        ):
            return True
        else:
            return False

# Class Method
date = Date.get_todays_date()

# Static Method
date = Date.print_date()


#check = Date(2023, 5, 29)