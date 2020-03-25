from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

class User(AbstractUser):
    USER_TYPE = [
        (0,"Admin"),
        (1,"Farmer"),
    ]
    user_type = models.IntegerField(choices=USER_TYPE,blank=False),
    age = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(100)])
