"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions, routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from catalog.views import CategoryView, ProductViewSet, ProductByCategory, UpdateCategoryView, UpdateProductView, \
    CreateCategoryView, DeleteCategoryView, CreateProductView, DeleteProductView, ProductView

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

router = routers.DefaultRouter()
# router.register(r'categories', CategoryViewSet)
# router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('categories/', CategoryView.as_view(), name="category"),
    path('categories/create/', CreateCategoryView.as_view(), name="create category"),
    path('categories/update/<int:pk>/', UpdateCategoryView.as_view(), name="update category"),
    path('categories/delete/<int:pk>/', DeleteCategoryView.as_view(), name="delete category"),
    path('categories/<int:pk>/products/', ProductByCategory.as_view(), name="products by category"),

    path('products/', ProductView.as_view(), name="product"),
    path('products/create/', CreateProductView.as_view(), name="create product"),
    path('products/update/<int:pk>/', UpdateProductView.as_view(), name="update product"),
    path('products/delete/<int:pk>/', DeleteProductView.as_view(), name="delete product"),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
