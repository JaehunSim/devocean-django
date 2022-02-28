from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200)
    field = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=500, blank=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    total_employees = models.IntegerField(blank=True, null=True)
    revenue = models.FloatField(blank=True, null=True)
    operating_income = models.FloatField(blank=True, null=True)
    net_income = models.FloatField(blank=True, null=True)
