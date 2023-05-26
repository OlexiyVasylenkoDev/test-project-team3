from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions, routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from order.views import OrderViewSet, OrderItemViewSet, TopSalesAPIView
from catalog.views import CategoryViewSet, ProductViewSet, CheckoutSessionView, SuccessfulPayment, stripe_session_completed_webhook, CategoryAttributeViewSet, ProductAttributeViewSet
from cart.views import CartView, AddToCartView, ClearCartView, RemoveFromCartView, CartViewSet, WishlistViewSet
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
main_router.register(r'top_sales', TopSalesAPIView)
main_router.register(r'category', CategoryViewSet)
main_router.register(r'category_attribute', CategoryAttributeViewSet)
main_router.register(r'product', ProductViewSet)
main_router.register(r'product_attribute', ProductAttributeViewSet)
main_router.register(r'review', ReviewViewSet)
main_router.register(r'cart', CartViewSet)
main_router.register(r'wishlist', WishlistViewSet)
main_router.register(r'distribution', EmailDistributionViewSet)
main_router.register(r'distribution_categories', DistributionCategoryViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(main_router.urls)),
    path('api/v1/authentication/', include("core.urls")),
    path('checkout/', CheckoutSessionView.as_view(), name='checkout'),
    path('stripe-session-completed/', stripe_session_completed_webhook, name='stripe-session-completed'),
    path('success/', SuccessfulPayment.as_view(), name='success'),
    path('api/v1/search/text/', text_search),
    path('api/v1/search/voice/', voice_search),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += [
    path('cart/', CartView.as_view(), name='cart_view'),
    path('cart/add/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/remove/<int:cart_item_id>/', RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('cart/clear/', ClearCartView.as_view(), name='clear_cart'),
]