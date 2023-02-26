from django.db import models

class data(models.Model):
    temp = models.IntegerField()
    humidity  = models.IntegerField()
    light_int =models.IntegerField()
    time = models.TimeField(auto_now_add=True)

class lights(models.Model):
    testlight = models.BooleanField()