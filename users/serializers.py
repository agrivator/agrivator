from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model   =   User
        fields  =   ('__all__')


class FarmerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model   =  Farmer
        fields  =  ('__all__')

class ShopSerializer(serializers.ModelSerializer):
    
    class Meta:
        model   =  Shop
        fields  =  ('__all__')

class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model   =  Customer
        fields  =  ('__all__')

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model   =  Product
        fields  =  ('__all__')
