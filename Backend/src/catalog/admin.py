from django.contrib import admin

from .models import Category, CategoryAttribute, Product, ProductAttribute


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


admin.site.register(Category, CategoryAdmin)
admin.site.register([CategoryAttribute, Product, ProductAttribute])
