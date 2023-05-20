import speech_recognition
from django.contrib.postgres.search import SearchVector, SearchQuery, TrigramSimilarity
from django.http import HttpResponse
from itertools import chain

from catalog.models import Product, Category
from core.models import SellerProfile


class Search:

    def perform_search(self, query):
        products_by_title = Product.objects.annotate(similarity=TrigramSimilarity("title", query), )\
            .filter(similarity__gt=0.1)\
            .order_by("-similarity")
        products_by_description = Product.objects.annotate(similarity=TrigramSimilarity("description", query), )\
            .filter(similarity__gt=0.1)\
            .order_by("-similarity")
        categories = Category.objects.annotate(similarity=TrigramSimilarity("title", query), )\
            .filter(similarity__gt=0.1)\
            .order_by("-similarity")
        sellers = SellerProfile.objects.annotate(similarity=TrigramSimilarity("name", query), )\
            .filter(similarity__gt=0.2)\
            .order_by("-similarity")
        results_chain = chain(products_by_title, products_by_description, categories, sellers)
        return set(results_chain)

    def text_search(self, request):
        query = request.GET.get('query')
        qs = self.perform_search(query)
        print([i for i in qs])
        return HttpResponse([str(i) + "\n" for i in qs])

    def voice_search(self, request):
        recognizer = speech_recognition.Recognizer()
        while True:
            try:
                with speech_recognition.Microphone() as mic:
                    recognizer.adjust_for_ambient_noise(source=mic, duration=0.2)
                    audio = recognizer.listen(mic)

                    text = recognizer.recognize_google(audio)
                    qs = self.perform_search(text)
                    print([i for i in qs])
                    if qs:
                        return HttpResponse([str(i) + "\n" for i in qs])
                    else:
                        continue
            except speech_recognition.UnknownValueError:
                recognizer = speech_recognition.Recognizer()
                continue
