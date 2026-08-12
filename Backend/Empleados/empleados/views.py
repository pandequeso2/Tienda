from rest_framework import viewsets, permissions
from .models import Empleado
from .serializers import EmpleadoSerializer

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all().order_by('id')
    serializer_class = EmpleadoSerializer
    permission_classes = [permissions.AllowAny]  # más adelante ajustamos permisos