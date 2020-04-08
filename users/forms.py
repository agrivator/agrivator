from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User,Farmer,Shop,Customer


class FarmerCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Farmer
        fields = ("email","first_name","last_name","phone_one")


class FarmerChangeForm(UserChangeForm):
    class Meta:
        model = Farmer
        fields = ("email","first_name","last_name","phone_one","phone_two","address")
