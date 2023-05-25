from django.contrib import admin

from . import models

from .tasks import promotion_prices, promotion_management


class ProductOnPromotion(admin.StackedInline):
    model = models.Promotion.products_on_promotion.through
    extra = 4
    raw_id_fields = ["product_id"]


class ProductList(admin.ModelAdmin):
    model = models.Promotion
    inlines = (ProductOnPromotion,)
    list_display = ("name", "is_active", "promo_start", "promo_end")

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        products_on_promotions = obj.products_on_promotion.through.objects.filter(promotion_id=obj.id)
        for product in products_on_promotions:
            product.product_id.save()
        promotion_prices.delay(obj.promo_reduction, obj.id)
        promotion_management.delay()


admin.site.register(models.Promotion, ProductList)
admin.site.register(models.PromoType)
admin.site.register(models.Coupon)


