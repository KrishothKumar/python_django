from rest_framework import serializers
from api_django.models import UserApis


# Creating serializers and inheriting UserApis class for .models.py (2nd) 
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserApis
        fields = '__all__'
