from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import ( FarmerCreationForm, FarmerChangeForm, 
                    ShopCreationForm, ShopChangeForm, 
                    CustomerCreationForm, CustomerChangeForm )

from .models import User, Farmer, Shop, Customer

#Farmer Admin
class FarmerAdmin(UserAdmin):
    add_form = FarmerCreationForm
    form = FarmerChangeForm
    model = Farmer
    list_display = ("email","is_active",)
    list_filter = ("email","is_active",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "age",
                    "phone_one",
                    "phone_two",
                    "address",
                    

                )
            },
        ),
        ("Permissions", {"fields": ("is_active","is_farmer")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    "age",
                    "email",
                    "phone_one",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)

#Shop ADmin
class ShopAdmin(UserAdmin):
    add_form = ShopCreationForm
    form = ShopChangeForm
    model = Shop
    list_display = ("email","is_active",)
    list_filter = ("email","is_active",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "email",
                    "shop_owner_name",
                    "address",
                    "phone_one",
                    "phone_two",
                    

                )
            },
        ),
        ("Permissions", {"fields": ("is_active","is_shop")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "name",
                    "email",
                    "shop_owner_name",
                    "address",
                    "phone_one",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)

class CustomerAdmin(UserAdmin):
    add_form = CustomerCreationForm
    form = CustomerChangeForm
    model = Customer
    list_display = ("email","is_active",)
    list_filter = ("email","is_active",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "email",
                    "phone_one",
                    "phone_two",
                    "address",
                    

                )
            },
        ),
        ("Permissions", {"fields": ("is_active","is_customer")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "name",
                    "address",
                    "email",
                    "phone_one",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(Farmer,FarmerAdmin)
admin.site.register(Shop,ShopAdmin)
admin.site.register(Customer,CustomerAdmin)

