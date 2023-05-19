from rest_framework import permissions
from rest_framework.permissions import BasePermission

from cart.models import WishList
from catalog.models import Product


class IsSeller(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.type == "seller")


class IsBuyer(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.type == "buyer")


class IsProductSeller(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and
                    request.user.type == "seller" and
                    Product.objects.get(pk=view.kwargs.get("pk")).created_by == request.user)


class IsProductBuyer(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and
                    request.user.type == "buyer" and
                    WishList.objects.get(pk=view.kwargs.get("pk")).user == request.user)


class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user.is_authenticated)
