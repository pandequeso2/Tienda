from rest_framework import serializers
from .models import Empleado

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ['id', 'user_id', 'nombre_empleado', 'cargo', 'salario', 'fecha_contratacion']