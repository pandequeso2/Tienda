from rest_framework import viewsets, permissions
from .models import Sede
from .serializers import SedeSerializer

class SedeViewSet(viewsets.ModelViewSet):
    queryset = Sede.objects.all().order_by('id')
    serializer_class = SedeSerializer
    permission_classes = [permissions.AllowAny]