import random

from django.shortcuts import render
from django.views import View

from .forms import GeneratorForm
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
        "gender": fname.gender
    }

    return result


class IndexView(View):
    """
    Return main page.
    """

    def get(self, request):
        """
        Render main page with an empty form.
        """

        context = {
            "form": GeneratorForm(label_suffix="")
        }
        return render(request, "app/index.html", context)
    
    def post(self, request):
        """
        Render main page with randomly selected data in form.
        """

        identity = draw_identity()
        context = {
            "form": GeneratorForm(initial=identity, label_suffix="")
        }

        return render(request, "app/index.html", context)
