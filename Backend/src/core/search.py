import speech_recognition
from django.contrib.postgres.search import TrigramSimilarity

from catalog.models import Product, Category
from catalog.serializers import CategorySerializer, ProductSerializer
from core.models import SellerProfile
from core.serializers import SellerSerializer


class Search:

    def perform_search(self, query):
        products = Product.objects.annotate(similarity=TrigramSimilarity("title", query) +
                                                       TrigramSimilarity("description", query)) \
            .filter(similarity__gt=0.1) \
            .order_by("-similarity")
        categories = Category.objects.annotate(similarity=TrigramSimilarity("title", query), ) \
            .filter(similarity__gt=0.1) \
            .order_by("-similarity")
        sellers = SellerProfile.objects.annotate(similarity=TrigramSimilarity("name", query), ) \
            .filter(similarity__gt=0.2) \
            .order_by("-similarity")
        category_serializer = CategorySerializer(categories, many=True)
        product_serializer = ProductSerializer(products, many=True)
        seller_serializer = SellerSerializer(sellers, many=True)
        result = category_serializer.data + product_serializer.data + seller_serializer.data
        return result

    def text_search(self, request):
        query = request.GET.get('query')
        return self.perform_search(query)

    def voice_search(self):
        recognizer = speech_recognition.Recognizer()
        while True:
            try:
                with speech_recognition.Microphone() as mic:
                    recognizer.adjust_for_ambient_noise(source=mic, duration=0.2)
                    audio = recognizer.listen(mic)

                    text = recognizer.recognize_google(audio)
                    qs = self.perform_search(text)
                    if qs:
                        return qs
                    else:
                        continue
            except speech_recognition.UnknownValueError:
                recognizer = speech_recognition.Recognizer()
                continue
