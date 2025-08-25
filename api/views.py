from django.shortcuts import render
from rest_framework import viewsets

from api.models import ApiUser, Warehouse, Product, Category
from api.serializers import UserSerializer, WarehouseSerializer, ProductSerializer, CategorySerializer


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = ApiUser.objects.all()
    http_method_names = ['post', 'get']
    serializer_class = UserSerializer

    authentication_classes = []
    permission_classes = []


class WarehouseModelViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer