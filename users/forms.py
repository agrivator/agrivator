from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User,Farmer,Shop,Customer

#Farmer Forms

class FarmerCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Farmer
        fields = ("email","first_name","last_name","phone_one","address")

class FarmerChangeForm(UserChangeForm):
    class Meta:
        model = Farmer
        fields = ("email","first_name","last_name","phone_one","phone_two","address")

#Shop Forms

class ShopCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Shop
        fields = ("email","name","shop_owner_name","phone_one","address")

class ShopChangeForm(UserChangeForm):
    class Meta:
        model = Farmer
        fields = ("email","name","shop_owner_name","phone_one","phone_two","address")

#Customer Forms

class CustomerCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Customer
        fields = ("email","name","address","phone_one")

class CustomerChangeForm(UserChangeForm):
    class Meta:
        model = Customer
        fields = ("email","name","address","phone_one","phone_two")
