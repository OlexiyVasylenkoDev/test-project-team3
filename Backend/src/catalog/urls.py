from django.urls import path, include
from rest_framework import routers

from catalog.views import CategoryViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'product', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
