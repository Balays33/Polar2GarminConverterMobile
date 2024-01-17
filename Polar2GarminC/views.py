from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

"""
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
"""

def index(request):
    """

    :param request:
    :return:
    """
    return render(request, 'Polar2GarminC/index.html', context={'hello': 'world'})



