from django.contrib import admin

# Register your models here.
from .models import data,lights
admin.site.register(lights)
admin.site.register(data)

