from rest_framework import serializers
from .models import data,lights 

class DataSerializer(serializers.ModelSerializer):
	class Meta:
		model = data
		fields ='__all__'

class Lightserializer(serializers.ModelSerializer):
	class Meta:
		model = lights
		fields ='__all__'