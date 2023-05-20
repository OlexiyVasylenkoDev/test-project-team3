from django.contrib import admin

from .models import DistributionCategory, EmailDistribution

admin.site.register(DistributionCategory)
admin.site.register(EmailDistribution)
