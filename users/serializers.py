from rest_framework import serializers
from .models import *


class FarmerProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model   =  FarmerProfile
        fields  =  ('__all__')

class ShopProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model   =  ShopProfile
        fields  =  ('__all__')

class CustomerProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model   =  CustomerProfile
        fields  =  ('__all__')

class ProductSerializer(serializers.ModelSerializer):

    farmer = serializers.HiddenField(
    default=serializers.CurrentUserDefault()
)
    
    class Meta:
        model   =  Product
        fields  =  ('__all__')
