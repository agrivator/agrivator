from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import User, FarmerProfile, ShopProfile, CustomerProfile, Product

admin.site.register(User)

admin.site.register(FarmerProfile)
admin.site.register(ShopProfile)
admin.site.register(CustomerProfile)
admin.site.register(Product)
