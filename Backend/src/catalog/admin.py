from django.contrib import admin

from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


admin.site.register([Category, Product, ], CategoryAdmin)
