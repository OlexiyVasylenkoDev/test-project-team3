from django.contrib import admin

from .models import Cart, WishList


admin.site.register([Cart, WishList, ])
