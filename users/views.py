from django.shortcuts import render

from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.response import Response

class UserViewset(viewsets.ModelViewSet):   # for user view.
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):

        #Save the post data when creating a new user.

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class FarmerViewset(viewsets.ModelViewSet):   # for user view.
    
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer

    def perform_create(self, serializer):

        #Save the post data when creating a new user.

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class ShopViewset(viewsets.ModelViewSet):   # for user view.
    
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def perform_create(self, serializer):

        #Save the post data when creating a new user.

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class CustomerViewset(viewsets.ModelViewSet):   # for user view.
    
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def perform_create(self, serializer):

        #Save the post data when creating a new user.

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class ProductViewset(viewsets.ModelViewSet):   # for user view.
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):

        #Save the post data when creating a new user.

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

