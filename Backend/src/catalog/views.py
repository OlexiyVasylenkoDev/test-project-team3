from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from catalog.models import Category, Product
from catalog.serializers import CategorySerializer, ProductSerializer
from core.permissions import IsSeller, IsProductSeller


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action in ('create', 'update', 'partial_update', 'destroy'):
            permission_classes = [IsAdminUser]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.action in ('create', 'destroy'):
            permission_classes = [IsSeller]
        elif self.action in ("update", "partial_update"):
            permission_classes = [IsProductSeller]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ProductsByCategory(ListAPIView):
    serializer_class = ProductSerializer
    allowed_methods = ["GET"]

    def get_queryset(self):
        category = self.kwargs["id"]
        return Product.objects.filter(category=category)

