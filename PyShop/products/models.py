from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image_url = models.CharField(max_length=2083)
    stock = models.IntegerField()


class Offer(models.Model):
    code = models.CharField(max_length=7)
    description = models.CharField(max_length=500)
    discount = models.FloatField()
