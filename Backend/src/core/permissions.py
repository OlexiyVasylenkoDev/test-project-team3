from rest_framework.permissions import BasePermission

from catalog.models import Product


class IsSeller(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.type == "seller")


class IsProductSeller(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and
                    request.user.type == "seller" and
                    Product.objects.get(pk=view.kwargs.get("pk")).created_by == request.user)
