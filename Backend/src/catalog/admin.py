from django.contrib import admin

from .models import Category, Product, Characteristic


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


admin.site.register([Category, Product, Characteristic, ])
