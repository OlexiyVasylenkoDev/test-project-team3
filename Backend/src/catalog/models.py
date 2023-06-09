from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models import Q
from statistics import fmean


from core.validators import validate_products_count, validate_product_price


class Category(models.Model):
    title = models.CharField(max_length=255, db_index=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class CategoryAttribute(models.Model):
    category = models.ManyToManyField(Category, related_name='attributes')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    count = models.IntegerField(default=1, validators=[validate_products_count, ])
    image = models.ImageField(upload_to='image/', blank=True)
    base_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_product_price, ])
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(to=get_user_model(), related_name='seller', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    @property
    def price(self):
        try:
            product_on_promotions = self.product_on_promotion.get(Q(promotion_id__is_active=True) & Q(product_id=self.id))
            return product_on_promotions.promo_price
        except ObjectDoesNotExist:
            return None
          
    def get_product_rating(self):
        ratings = [review.rating for review in self.reviews.all()]
        return fmean(ratings)


class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, related_name='attributes', on_delete=models.CASCADE)
    attribute = models.ForeignKey(CategoryAttribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.product}. {self.attribute}: {self.value}"
      
