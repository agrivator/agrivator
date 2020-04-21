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

USER_CHOICES = [
    ('Farmer','Farmer'),
    ('Shop','Shop'),
    ('Customer','Customer'),
]

"""
Currently Only super user gets to view admin dashboard
Staff Users can login to admin but no permission to view anything
Non Staff users are the end users the farmers

"""


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200,unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)],null=True)
    phone_one = models.CharField(max_length=14, validators=[phone_number_regex])
    email = models.EmailField(_("email address"), unique=True, primary_key=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    user_type = models.CharField(choices=USER_CHOICES,max_length=50)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ['first_name','last_name','user_type','age']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class FarmerProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    farm_address = models.TextField(max_length=500)
    farm_phone = models.CharField(max_length=14, validators=[phone_number_regex])

    def __str__(self):
        return (f"{self.user}")
    

class ShopProfile(models.Model):
    shop_name = models.CharField(max_length=255)
    shop_owner_name = models.ForeignKey(User,on_delete=models.CASCADE)
    shop_address = models.TextField(max_length=500)
    shop_phone = models.CharField(max_length=14, validators=[phone_number_regex])

    def __str__(self):
        return self.shop_name

class CustomerProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    customer_address = models.TextField(max_length=500)
    
    def __str__(self):
        return self.user


class Product(models.Model):
    name = models.CharField(max_length=100)
    cost = models.FloatField()
    quantity = models.FloatField()
    organic = models.BooleanField()
    farmer = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name
