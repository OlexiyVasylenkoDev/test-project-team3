# DRF
from rest_framework.viewsets import ModelViewSet

# Models
from cart.models import Cart, WishList, CartItem
from catalog.models import Product

from cart.serializers import CartSerializer, WishlistSerializer, CartItemSerializer
from core.permissions import IsProductBuyer, IsBuyer

# Django
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, RedirectView


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer



class CartItemViewSet(ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def get_permissions(self):
        if self.action in ('create', 'destroy'):
            permission_classes = [IsProductBuyer]
        elif self.action in ("update", "partial_update"):
            permission_classes = [IsProductBuyer]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


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


def merge_carts(user, session_cart):
    if user.is_authenticated:
        user_cart = Cart.objects.filter(user=user).first()
        if user_cart:
            for item in session_cart.cart_items.all():
                cart_item, created = CartItem.objects.get_or_create(cart=user_cart, product=item.product)
                if created:
                    cart_item.quantity = item.quantity
                else:
                    cart_item.quantity += item.quantity
                cart_item.save()
            session_cart.cart_items.all().delete()
            session_cart.delete()
        else:
            # This should only happen when the user has no cart associated with them
            # We associate the current session cart with the user
            session_cart.user = user
            session_cart.save()
            user_cart = session_cart
        return user_cart
    return session_cart


def get_cart_from_session(request):
    cart_id = request.session.get('cart_id')
    user = request.user if request.user.is_authenticated else None

    if user:
        user_cart = Cart.objects.filter(user=user).first()
        if user_cart:
            cart = user_cart
        else:
            if not cart_id or not Cart.objects.filter(id=cart_id).exists():
                cart = Cart.objects.create(user=user)
            else:
                cart = Cart.objects.get(id=cart_id)
    else:
        if not cart_id or not Cart.objects.filter(id=cart_id).exists():
            cart = Cart.objects.create()
        else:
            cart = Cart.objects.get(id=cart_id)

    request.session['cart_id'] = cart.id
    return cart


class CartView(TemplateView):
    template_name = 'cart/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = get_cart_from_session(self.request)
        context['cart'] = cart
        return context


class AddToCartView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        product_id = self.kwargs['product_id']

        product = get_object_or_404(Product, id=product_id)
        cart = get_cart_from_session(self.request)

        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity += 1
        cart_item.save()
        cart.cart_items.add(cart_item)

        return reverse('cart_view')


class RemoveFromCartView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        cart_item_id = self.kwargs['cart_item_id']
        cart = get_cart_from_session(self.request)

        cart_item = get_object_or_404(CartItem, id=cart_item_id, cart=cart)
        cart_item.delete()

        return reverse('cart_view')


class ClearCartView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        cart = get_cart_from_session(self.request)
        cart.cart_items.all().delete()
        return reverse('cart_view')
