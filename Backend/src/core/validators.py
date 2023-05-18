from django.core.exceptions import ValidationError


def validate_product_price(price):
    if price < 0:
        raise ValidationError("Price cannot be negative!")


def validate_products_count(count):
    if count < 0:
        raise ValidationError("Products count cannot be negative!")
