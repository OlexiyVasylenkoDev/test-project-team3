import speech_recognition
from django.contrib.postgres.search import SearchVector, SearchQuery
from django.http import HttpResponse
from itertools import chain

from catalog.models import Product, Category
from core.models import SellerProfile


class Search:
    products = Product.objects.all()
    categories = Category.objects.all()
    sellers = SellerProfile.objects.all()

    def perform_search(self, query):
        products = Product.objects.annotate(search=SearchVector("title", "description")).filter(search=SearchQuery(query))
        categories = Category.objects.annotate(search=SearchVector("title")).filter(search=SearchQuery(query))
        sellers = SellerProfile.objects.annotate(search=SearchVector("name")).filter(search=SearchQuery(query))

        results_chain = chain(products, categories, sellers)
        return results_chain

    def text_search(self, request):
        query = request.GET.get('query')
        qs = self.perform_search(query)
        print(qs)
        return HttpResponse(qs)

    def voice_search(self, request):
        recognizer = speech_recognition.Recognizer()
        while True:
            try:
                with speech_recognition.Microphone() as mic:
                    recognizer.adjust_for_ambient_noise(source=mic, duration=0.2)
                    audio = recognizer.listen(mic)

                    text = recognizer.recognize_google(audio)
                    text = text.lower()
                    print(text)
                    qs = self.perform_search(text)
                    print(qs)
                    if qs:
                        return HttpResponse([str(i) + "\n" for i in qs])
                    else:
                        continue
            except speech_recognition.UnknownValueError:
                recognizer = speech_recognition.Recognizer()
                continue
