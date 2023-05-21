from .search import Search
from .serializers import RegistrationSerializer
from rest_framework import generics


class Registration(generics.CreateAPIView):
    serializer_class = RegistrationSerializer


def text_search(request):
    search = Search()
    return search.text_search(request)


def voice_search(request):
    search = Search()
    return search.voice_search(request)
