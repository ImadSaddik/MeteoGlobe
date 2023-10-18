from rest_framework import serializers
from .models import Meteorite


class MeteoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meteorite
        fields = '__all__'
