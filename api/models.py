from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CASCADE
from rest_framework.fields import CharField

#Создадим категорию пользователя
class Category(models.Model):
    name = models.CharField(max_length=60)


# Создаем модель пользователь
class ApiUser(AbstractUser):
    cat = models.ForeignKey(Category, related_name='users', on_delete=CASCADE)


    def __str__(self):
        return f'user {self.username}: {self.cat}'


#Создаем модель "склад"
class Warehouse(models.Model):
    name = models.CharField(max_length=128)
    user = models.ForeignKey(ApiUser,related_name='warehouses', on_delete=CASCADE)

    def __str__(self):
        return f'{self.id}: {self.name}'


# Создаем модель "продукт"
class Product(models.Model):
    name = models.CharField(max_length=128)
    warehouse = models.ForeignKey(Warehouse, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.warehouse.name}- product{self.name}'

