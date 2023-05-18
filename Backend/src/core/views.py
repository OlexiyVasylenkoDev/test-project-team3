from django.shortcuts import render
from .serializers import RegistrationSerializer
from rest_framework import generics


class Registration(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
