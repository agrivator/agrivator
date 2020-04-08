from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from .managers import CustomUserManager

"""
Currently Only super user gets to view admin dashboard
Staff Users can login to admin but no permission to view anything
Non Staff users are the end users the farmers

"""


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    phone_number_regex = RegexValidator(
        regex="^((\+91|91|0)[\- ]{0,1})?[456789]\d{9}$",
        message="Please Enter 10/11 digit mobile number or landline as 0<std code><phone number>",
        code="invalid_mobile",
    )
    phone = models.CharField(max_length=14, validators=[phone_number_regex])
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "age"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    class Meta:
        abstract = True
class Farmer(User):
    Area = models.FloatField()
    Pesticide =models.BooleanField()
    Nutrients = models.CharField(max_length=200)
class Product(models.Model):
    Name = models.CharField(max_length=100)
    Cost = models.FloatField()
    Pesticide = models.BooleanField()
    Quantity = models.FloatField()
    