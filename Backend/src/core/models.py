from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField

from core.managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    class UserTypeChoices(models.TextChoices):
        SELLER = "seller", _("seller")
        BUYER = "buyer", _("buyer")

    type = models.CharField(
        max_length=6,
        choices=UserTypeChoices.choices,
        null=True,
        blank=True,
    )
    email = models.EmailField(
        _("email"),
        unique=True,
        blank=False
    )
    phone = PhoneNumberField(
        _("phone"),
        null=True,
        blank=True,
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. " "Unselect this instead of deleting accounts."
        ),
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


class Profile(models.Model):
    class Meta:
        abstract = True

    user = models.OneToOneField(
        to=get_user_model(),
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    name = models.CharField(
        _("name"),
        max_length=256,
        null=True,
        blank=False,
    )
    photo = models.ImageField(
        _("photo"),
        upload_to="?", # WHERE DO WE STORE STATIC FILES?
        null=True,
        blank=True,
    )


class BuyerProfile(Profile):
    class UserGenderChoices(models.TextChoices):
        MALE = "male", _("male")
        FEMALE = "female", _("female")
        OTHER = "other", _("other")

    gender = models.CharField(
        max_length=6,
        choices=UserGenderChoices.choices,
    )
    date_of_birth = models.DateTimeField(
        auto_now_add=False,
        default=None,
        null=True,
        blank=True,
    )

    def age(self):
        return timezone.now() - self.date_of_birth


class SellerProfile(Profile):
    website = models.URLField()
    is_resident = models.BooleanField(
        default=True,
        null=False,
        blank=True,
    )
