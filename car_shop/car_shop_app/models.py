from django.db import models

class Car(models.Model):
    brand_name = models.CharField(max_length=50)
    model_name = models.CharField(max_length=50)
    year = models.IntegerField()
    engine = models.FloatField()
    price = models.FloatField()
