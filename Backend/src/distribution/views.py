
from rest_framework import viewsets, status
from rest_framework.permissions import IsAdminUser

from .models import DistributionCategory, EmailDistribution
from .serializers import DistributionCategorySerializer, EmailDistributionSerializer


class DistributionCategoryViewSet(viewsets.ModelViewSet):
    queryset = DistributionCategory.objects.all()
    serializer_class = DistributionCategorySerializer

    def get_permissions(self):
        if self.action in ('create', 'update', 'partial_update', 'destroy'):
            permission_classes = [IsAdminUser]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

class EmailDistributionViewSet(viewsets.ModelViewSet):
    queryset = EmailDistribution.objects.all()
    serializer_class = EmailDistributionSerializer

    def get_permissions(self):
        if self.action in ('create', 'update', 'partial_update', 'destroy'):
            permission_classes = [IsAdminUser]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]
