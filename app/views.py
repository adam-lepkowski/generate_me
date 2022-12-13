from django.shortcuts import render
from django.views import View

from .forms import GeneratorForm
from .utils import draw_identity


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
            "form": GeneratorForm(initial=identity, label_suffix=""),
            "gender": identity.get("gender")
        }
        return render(request, "app/index.html", context)
