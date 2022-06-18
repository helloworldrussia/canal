from django.db import models


class Table(models.Model):
    order_id = models.IntegerField()
    price_usd = models.FloatField()
    price_rub = models.FloatField()
    delivery_date = models.DateField()


class TableBuffer(models.Model):
    order_id = models.IntegerField()
    price_usd = models.FloatField()
    price_rub = models.FloatField()
    delivery_date = models.DateField()
