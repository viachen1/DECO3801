from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('notes', index),
    path('sessions', index),
]
