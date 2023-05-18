from django.db import models
# from django.core.mail import send_mail
from django.contrib.auth.models import User


class EmailDistribution(models.Model):
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=3000)
