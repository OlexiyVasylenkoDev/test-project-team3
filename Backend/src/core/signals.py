from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver

from cart.models import Cart
from cart.views import merge_carts


@receiver(user_logged_in)
def handle_user_login(sender, user, request, **kwargs):
    session_cart_id = request.session.get('cart_id')
    if session_cart_id and Cart.objects.filter(id=session_cart_id).exists():
        session_cart = Cart.objects.get(id=session_cart_id)
        merge_carts(user, session_cart)
