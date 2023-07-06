from django.db import models

# Create your models here.
class Passenger(models.Model):
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=20)
    travelPoints = models.IntegerField()