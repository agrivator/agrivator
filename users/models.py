from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from .managers import CustomUserManager

phone_number_regex = RegexValidator(
        regex="^((\+91|91|0)[\- ]{0,1})?[456789]\d{9}$",
        message="Please Enter 10/11 digit mobile number or landline as 0<std code><phone number>",
        code="invalid_mobile",
    )

"""
Currently Only super user gets to view admin dashboard
Staff Users can login to admin but no permission to view anything
Non Staff users are the end users the farmers

"""


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True, primary_key=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Farmer(User):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    phone_one = models.CharField(max_length=14, validators=[phone_number_regex])
    phone_two = models.CharField(max_length=14, validators=[phone_number_regex],null=True, blank=True)
    address = models.TextField(max_length=500)
    is_farmer = models.BooleanField(default=True)
    

class Shop(User):
    name = models.CharField(max_length=255)
    address = models.TextField(max_length=500)
    shop_owner_name = models.CharField(max_length=255)
    phone_one = models.CharField(max_length=14, validators=[phone_number_regex])
    phone_two = models.CharField(max_length=14, validators=[phone_number_regex],null=True, blank=True)
    is_shop = models.BooleanField(default=True)


class Customer(User):
    name = models.CharField(max_length=255)
    address = models.TextField(max_length=500)
    phone_one = models.CharField(max_length=14, validators=[phone_number_regex])
    phone_two = models.CharField(max_length=14, validators=[phone_number_regex],null=True, blank=True)
    is_customer = models.BooleanField(default=True)


class Product(models.Model):
    name = models.CharField(max_length=100)
    cost = models.FloatField()
    quantity = models.FloatField()
    organic = models.BooleanField()
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE,null=True)
