from django.contrib import admin

from . import models


class ProductOnPromotion(admin.StackedInline):
    model = models.Promotion.products_on_promotions.through
    extra = 4
    raw_id_fields = ["product_id"]


class ProductList(admin.ModelAdmin):
    model = models.Promotion
    inlines = (ProductOnPromotion,)
    list_display = ("name", "is_active", "promo_start", "promo_end")


admin.site.register(models.Promotion, ProductList)
admin.site.register(models.PromoType)
admin.site.register(models.Coupon)


