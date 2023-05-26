from rest_framework.decorators import api_view
from rest_framework.response import Response
from .search import Search
from .serializers import RegistrationSerializer
from rest_framework import generics


class Registration(generics.CreateAPIView):
    serializer_class = RegistrationSerializer


@api_view(["GET"])
def text_search(request):
    search = Search()
    return Response(search.text_search(request))

@api_view(["GET"])
def voice_search(request):
    search = Search()
    return Response(search.voice_search())
