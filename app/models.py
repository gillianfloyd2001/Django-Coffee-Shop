from django.db import models
from datetime import datetime

# Create your models here.


class Coffee(models.Model):
    name = models.TextField()
    price = models.FloatField()


class Transaction(models.Model):
    time = models.DateTimeField()
    item = models.ForeignKey(Coffee, on_delete=models.PROTECT)
    pre_tax = models.FloatField()
    tax = models.FloatField()
