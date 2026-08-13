from rest_framework import serializers
from .models import Sede

class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sede
        fields = [
            'id', 'nombre', 'direccion', 'comuna',
            'region', 'telefono', 'fecha_apertura', 'activa',
        ]