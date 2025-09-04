from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api.models import ApiUser, Warehouse, Product, Category, Basket
from api.serializers import UserSerializer, WarehouseSerializer, ProductSerializer, CategorySerializer, BasketSerializer


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

    @action(detail=True)
    def products(self, request, pk=None):
        warehouse = get_object_or_404(Warehouse.objects.all(), id=pk)
        free_products = warehouse.products.filter(quantity__gt=0)
        return Response(
            ProductSerializer(free_products, many=True).data
        )


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer




class BasketModelViewSet(viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer


