from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import FarmerCreationForm, FarmerChangeForm
from .models import User, Farmer, Shop, Customer


class FarmerAdmin(UserAdmin):
    add_form = FarmerCreationForm
    form = FarmerChangeForm
    model = Farmer
    list_display = (
        
        "email",
        "is_active",
    )
    list_filter = (
        "email",
        "is_active",
    )
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
        ("Permissions", {"fields": ("is_staff", "is_active","is_farmer")}),
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
                    "is_farmer",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)

admin.site.register(User)

admin.site.register(Farmer,FarmerAdmin)
admin.site.register(Shop)
admin.site.register(Customer)

