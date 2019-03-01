from django.db import models
from django_mysql.models import JSONField




class WeatherDataModel(models.Model):
    location = models.CharField(max_length=29)
    tmax = JSONField()
    tmin = JSONField()
    rainfall = JSONField()


"""

class UKLocation(models.Model):
    tmax = JSONField()
    tmin = JSONField()
    rainfall = JSONField()

class EnglandLocation(models.Model):
    tmax = JSONField()
    tmin = JSONField()
    rainfall = JSONField()

class ScotlandLocation(models.Model):
    tmax = JSONField()
    tmin = JSONField()
    rainfall = JSONField()

class WalesLocation(models.Model):
    tmax = JSONField()
    tmin = JSONField()
    rainfall = JSONField()
"""
