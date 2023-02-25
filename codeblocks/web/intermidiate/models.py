from django.db import models

# Create your models here.

class Url(models.Model):
    url = models.CharField(max_length=250)
    short_id = models.CharField(max_length=10)
    creation_date = models.DateTimeField(auto_now_add=True)
