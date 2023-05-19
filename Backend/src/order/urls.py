from django.urls import path, include
from order.views import OrderViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Order', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]