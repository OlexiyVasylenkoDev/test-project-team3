from django.contrib import admin

# Register your models here.
from core.models import User, SellerProfile, BuyerProfile

admin.site.register([User, SellerProfile, BuyerProfile])