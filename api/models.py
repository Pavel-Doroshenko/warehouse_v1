from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CASCADE
from rest_framework.fields import CharField

#Создадим категорию пользователя
class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return f'{self.name}'


# Создаем модель пользователь
class ApiUser(AbstractUser):
    cat = models.ForeignKey(Category, related_name='users', verbose_name='Категория пользователя',  on_delete=CASCADE)
    #Категория пользователя: 1-поставщик, 2-покупатель

    def __str__(self):
        return f'user {self.username} : {self.cat.name}'


#Создаем модель "склад"
class Warehouse(models.Model):
    name = models.CharField(max_length=128)
    user = models.ForeignKey(ApiUser,related_name='warehouses', on_delete=CASCADE)

    def __str__(self):
        return f'{self.id} : {self.name}'


# Создаем модель "продукт"
class Product(models.Model):
    name = models.CharField(max_length=128)
    quantity = models.IntegerField(null=True)
    warehouse = models.ForeignKey(Warehouse, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.warehouse.name} - {self.name}'


class Basket(models.Model):
    product = models.ForeignKey(Product, related_name='baskets', on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)
    user = models.ForeignKey(ApiUser, related_name='baskets', on_delete=CASCADE)

    def __str__(self):
        return f'{self.user} ; {self.product.name} = {self.quantity}'

