from django.db import models


# Create your models here.
class Predictions(models.Model):
    address = models.CharField(max_length=200)
    crime_date = models.CharField(max_length=100)
    hour = models.CharField(max_length=100)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    predicted_case = models.CharField(max_length=300)

    def __str__(self):
        return self.address
