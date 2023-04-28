from django.shortcuts import render
from django.http import JsonResponse
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

        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            identity = draw_identity()
            return JsonResponse(identity)

        context = {
            "form": GeneratorForm(label_suffix="")
        }
        return render(request, "app/index.html", context)

