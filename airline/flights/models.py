from django.db import models

# Create your models here.
# every model will be a Python class
class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()