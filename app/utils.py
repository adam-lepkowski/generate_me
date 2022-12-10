import random

from .models import FirstNameModel, LastNameModel

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