import os
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


def images():
    return os.path.join(settings.MEDIA_ROOT, 'images')


class CustomUser(AbstractUser):
    pass


class Yogurt(models.Model):
    name = models.CharField(max_length=55)
    compound = models.TextField(max_length=250)
    description = models.TextField(max_length=250)
    mass = models.FloatField()
    protein = models.FloatField()
    fats = models.FloatField()
    carbohydrates = models.FloatField()
    kcal = models.FloatField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to=images(), null=True)

    def __str__(self):
        return self.name


class City(models.Model):

    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class Order(models.Model):

    user = models.ForeignKey(CustomUser, related_name='user', on_delete=models.CASCADE)
    city = models.CharField(max_length=55, default='Bishkek', null=True)
    address = models.CharField(max_length=55, null=True)
    user_email = models.EmailField(max_length=55, null=True)
    user_first_name = models.CharField(max_length=25, null=True)
    user_last_name = models.CharField(max_length=25, null=True)
    yogurt = models.ForeignKey(Yogurt, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, null=True)


