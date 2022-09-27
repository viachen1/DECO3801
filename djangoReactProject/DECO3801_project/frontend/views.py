from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def index(request, *args, **kwargs):
    return render(request,'frontend/index.html')
