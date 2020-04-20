from django.shortcuts import render

from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.response import Response



class FarmerViewset(viewsets.ModelViewSet):   # FarmerProfile Creation
    
    queryset = FarmerProfile.objects.all()
    serializer_class = FarmerProfileSerializer

    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        #Save the post data when creating a new user.

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class ShopViewset(viewsets.ModelViewSet):   # Shop Profile Creation
    
    queryset = ShopProfile.objects.all()
    serializer_class = ShopProfileSerializer

    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        #Save the post data when creating a new user.

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class CustomerViewset(viewsets.ModelViewSet):   # Customer Profile Creation
    
    queryset = CustomerProfile.objects.all()
    serializer_class = CustomerProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        #Save the post data when creating a new user.

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class ProductViewset(viewsets.ModelViewSet):   # Product Creation only for farmer user

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        #Save the post data when creating a new user.

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

