from datetime import datetime
from decimal import Decimal
from math import ceil

from celery import shared_task
from django.db import transaction
from django.db.models import Q

from .models import Promotion


@shared_task()
def promotion_prices(reduction_amount, obj_id):
    with transaction.atomic():
        promotions = Promotion.products_on_promotion.through.objects.filter(promotion_id=obj_id)
        reduction = reduction_amount / 100

        for promo_product in promotions:
            if not promo_product.price_override:
                price = promo_product.product_id.base_price
                print(price)
                new_price = ceil(price - (price * Decimal(reduction)))
                promo_product.promo_price = Decimal(new_price)
                promo_product.save()


@shared_task()
def promotion_management():
    with transaction.atomic():
        promotions = Promotion.objects.filter(is_schedule=True)

        now = datetime.now().date()

        for promo in promotions:
            if promo.is_schedule:
                if promo.promo_end < now:
                    promo.is_active = False
                    promo.is_schedule = False
                else:
                    if promo.promo_start <= now:
                        promo.is_active = True
                    else:
                        promo.is_active = False
            promo.save()


# @shared_task()
# def promotion_prices_to_zero(obj_id):
#     with transaction.atomic():
#         promotions = Promotion.products_on_promotion.through.objects.filter(promotion_id=obj_id)
#         for promo_product in promotions:
#             pr
#             promo_product.save()
