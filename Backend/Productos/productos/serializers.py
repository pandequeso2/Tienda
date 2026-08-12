from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = [
            'id', 'nombre', 'descripcion', 'sku',
            'precio', 'stock', 'sede_id', 'activo', 'fecha_creacion',
        ]