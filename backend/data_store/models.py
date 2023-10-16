from django.db import models


class Meteorite(models.Model):
    mass = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    name_type = models.CharField(max_length=100)
    recorded_class = models.CharField(max_length=100)
    discovery_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name
