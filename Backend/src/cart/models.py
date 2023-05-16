from django.db import models
from uuid import uuid4


class Cart(models.Model):
    id = models.AutoField(primary_key=True, default=1000000)
    #goods = models.ForeignKey


class WishList(models.Model):
    id = models.AutoField(primary_key=True, default=1000000)
    # user = models.ForeignKey
    # goods = models.ForeignKey
