from django.shortcuts import render
from django.views import View

from .forms import GeneratorForm

# Create your views here.



class IndexView(View):
    """
    Return main page.
    """

    def get(self, request):
        context = {
            "form": GeneratorForm(label_suffix="")
        }
        return render(request, "app/index.html", context)
    
    def post(self, request):
        context = {
            "form": GeneratorForm(label_suffix="")
        }
        return render(request, "app/index.html", context)
