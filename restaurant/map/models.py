from django.db import models

# Create your models here.


class Restaurant(models.Model):

    name = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=200)
    short_description = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    latitude = models.FloatField()
    longitude = models.FloatField()
