from re import split


class Error(Exception):
    pass


class DayException(Error):
    pass


class MonthException(Error):
    pass


class YearException(Error):
    pass


class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def date_to_int(cls, date):
        return [int(x) for x in split('-', date)]

    @staticmethod
    def validate_date(date):
        try:
            if Date.date_to_int(date)[0] < 1 or Date.date_to_int(date)[0] > 31:
                raise DayException
            if Date.date_to_int(date)[1] < 1 or Date.date_to_int(date)[1] > 12:
                raise MonthException
            elif Date.date_to_int(date)[2] < 0:
                raise YearException
            else:
                return True
        except DayException:
            return "Day number is not valid!"
        except MonthException:
            return "Month number is not valid!"
        except YearException:
            return "Year number is not valid!"


my_date = "12-01-2022"
if Date.validate_date(my_date):
    print(*Date.date_to_int(my_date))
