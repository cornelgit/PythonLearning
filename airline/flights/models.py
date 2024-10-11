from django.db import models

# Create your models here.
# every model will be a Python class
class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()

    # return a string representation of this object
    def __str__(self):
        return (f"{self.id}: {self.origin} to {self.destination}")