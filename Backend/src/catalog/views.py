from django.shortcuts import render

# Create your views here.
from requests import Response
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from catalog.models import Category, Product
from catalog.serializers import CategorySerializer, ProductSerializer, ProductsByCategorySerializer, \
    UpdateProductSerializer
from core.permissions import IsSeller, IsProductSeller


class BaseCategoryView:
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryView(BaseCategoryView, ListAPIView, ):
    pass


class CreateCategoryView(BaseCategoryView, CreateAPIView):
    permission_classes = [IsAdminUser, ]


class UpdateCategoryView(BaseCategoryView, UpdateAPIView):
    permission_classes = [IsAdminUser, ]


class DeleteCategoryView(BaseCategoryView, DestroyAPIView):
    permission_classes = [IsAdminUser, ]


class BaseProductView:
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductView(BaseProductView, ListAPIView, ):
    pass


class CreateProductView(BaseProductView, CreateAPIView):
    permission_classes = [IsSeller, ]




class UpdateProductView(BaseProductView, UpdateAPIView):
    permission_classes = [IsProductSeller, ]


class DeleteProductView(BaseProductView, DestroyAPIView):
    permission_classes = [IsSeller, ]


class ProductViewSet(BaseProductView, ModelViewSet, ):
    pass


class UpdateProductView(UpdateAPIView, ):
    queryset = Product.objects.all()
    permission_classes = [IsProductSeller, ]
    serializer_class = UpdateProductSerializer


class ProductByCategory(ListAPIView):
    def get_queryset(self):
        print(self.request.query_params)
        return Product.objects.all()
        # return Product.objects.filter(category=self.request.query_params["pk"])

    serializer_class = ProductsByCategorySerializer
