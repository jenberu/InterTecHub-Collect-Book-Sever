from rest_framework import serializers
from .models import Bookes
class BookSerialzer(serializers.ModelSerializer):
    class Meta:
        model=Bookes
        fields='__all__'
        