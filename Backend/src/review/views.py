from rest_framework import viewsets, status
from rest_framework.response import Response
from permissions import IsAuthenticated

from .models import Review
from .serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    def update(self, request, *args, **kwargs):
        review = self.get_object()
        if review.user != request.user:
            return Response({'message': 'Not found', 'status': '404'}, status=status.HTTP_404_NOT_FOUND, )
        return super(ReviewViewSet, self).update(request, *args, **kwargs)


    def destroy(self, request, *args, **kwargs):
        review = self.get_object()
        if review.user != request.user:
            return Response({'message': 'Not found', 'status': '404'}, status=status.HTTP_404_NOT_FOUND, )
        return super(ReviewViewSet, self).destroy(request, *args, **kwargs)