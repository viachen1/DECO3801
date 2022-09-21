from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    """ View function for homepage """
    return HttpResponse("Index here.")
