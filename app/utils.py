import random
import datetime

from .models import FirstNameModel, LastNameModel


def is_leap(year):
    """
    Check if year is a leap year.

    Returns
    ----------
    bool
    """

    if (year % 400 == 0) and (year % 100 == 0):
        return True
    elif (year % 4 ==0) and (year % 100 != 0):
        return True
    return False


def draw_dob():
    """
    Draw a random date of birth.

    Returns
    ----------
    str
        dob in format yyyy-mm-dd
    """

    year = random.randint(1970, 2010)
    month = random.randint(1, 12)
    days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    day = random.randint(1, days[month])
    dob = datetime.date(year, month, day).strftime("%Y-%m-%d")
    return dob 

def draw_identity():
    """
    Draw a random identity from FirstNameModel and LastNameModel.

    Returns
    ----------
    dict
        a random identity
    """

    min_val = 1
    max_fname = FirstNameModel.objects.order_by("-id")[0].id
    fname_id = random.randint(min_val, max_fname)
    fname = FirstNameModel.objects.get(id=fname_id)
    lname_ids = [
        l.id for l in LastNameModel.objects.filter(gender=fname.gender)]
    lname_id = random.choice(lname_ids)
    lname = LastNameModel.objects.get(id=lname_id)
    result = {
        "first_name": fname.first_name,
        "last_name": lname.last_name,
        "gender": fname.gender,
    }

    return result