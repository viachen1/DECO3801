from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *


class SessionView(generics.CreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
