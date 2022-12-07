from django.shortcuts import render

from .forms import GeneratorForm

# Create your views here.


def index(request):
    """
    Return main page.
    """
    
    context = {
        "form": GeneratorForm(label_suffix="")
    }
    return render(request, "app/index.html", context)