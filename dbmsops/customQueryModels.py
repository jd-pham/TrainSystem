from django.db import models

class Query1Model(models.Model):
    passenger_id = models.IntegerField()

class Query2Model(models.Model):
    amount = models.FloatField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class Query3Model(models.Model):
    full_name = models.CharField(max_length=100)
    no_of_tickets = models.IntegerField()

class Query4Model(models.Model):
    station_name = models.CharField(max_length=100)
    no_of_trains = models.IntegerField()