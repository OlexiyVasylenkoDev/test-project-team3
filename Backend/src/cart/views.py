from rest_framework.viewsets import ModelViewSet

from cart.models import Cart, WishList
from cart.serializers import CartSerializer, WishlistSerializer
from core.permissions import IsProductBuyer, IsBuyer


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class WishlistViewSet(ModelViewSet):
    queryset = WishList.objects.all()
    serializer_class = WishlistSerializer

    def get_permissions(self):
        if self.action in ('create', 'destroy'):
            permission_classes = [IsBuyer]
        elif self.action in ("update", "partial_update"):
            permission_classes = [IsProductBuyer]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
