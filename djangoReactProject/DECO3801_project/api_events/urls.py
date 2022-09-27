from .views import *
from django.urls import path, include

urlpatterns = [
   path('session/api', SessionView.as_view()),
]
