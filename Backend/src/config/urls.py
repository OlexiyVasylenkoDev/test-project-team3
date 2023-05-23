from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions, routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from cart.views import CartViewSet, WishlistViewSet
from catalog.views import CategoryViewSet, ProductViewSet
from order.views import OrderViewSet, OrderItemViewSet
from core.views import text_search, voice_search
from review.views import ReviewViewSet
from distribution.views import DistributionCategoryViewSet, EmailDistributionViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

main_router = routers.DefaultRouter()
main_router.register(r'order', OrderViewSet)
main_router.register(r'order_item', OrderItemViewSet)
main_router.register(r'category', CategoryViewSet)
main_router.register(r'product', ProductViewSet)
main_router.register(r'review', ReviewViewSet)
main_router.register(r'cart', CartViewSet)
main_router.register(r'wishlist', WishlistViewSet)
main_router.register(r'distribution', EmailDistributionViewSet)
main_router.register(r'distribution_categories', DistributionCategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/text/', text_search),
    path('search/voice/', voice_search),
    path('api/v1/', include(main_router.urls)),
    path('api/v1/authentication/', include("core.urls")),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
