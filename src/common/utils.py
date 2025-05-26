from datetime import datetime


def date_to_str(value, format):
    return datetime.strptime(value, "%Y-%m-%d").date().strftime(format)


def datetime_to_str(value, format):
    return datetime.strptime(value, "%Y-%m-%d %H:%M:%S.%f").strftime(format)

def str_to_datetime(value, format):
    return datetime.strptime(value, format)

def str_to_date(value, format):
    return datetime.strptime(value, format).date()