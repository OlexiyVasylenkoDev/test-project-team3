from rest_framework import viewsets
from .models import Review
from .permissions import IsLogged
from .serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsLogged]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
