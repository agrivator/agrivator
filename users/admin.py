from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import User, Farmer, Product


class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = Farmer
    list_display = (
        
        "email",
        "is_farmer",
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
                    "phone",
                    "email",
                    "is_farmer",

                )
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "phone",
                    "is_farmer",
                    "password1",
                    "password2",
                    "is_active",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(Farmer, UserAdmin)

