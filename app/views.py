from django.shortcuts import render

# Create your views here.


def index(request):
    """
    Return main page.
    """
    
    return render(request, "app/index.html")