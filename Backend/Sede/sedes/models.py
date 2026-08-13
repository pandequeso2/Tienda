from django.db import models

class Sede(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre de la Sede")
    direccion = models.CharField(max_length=255, verbose_name="Dirección")
    comuna = models.CharField(max_length=100, verbose_name="Comuna")
    region = models.CharField(max_length=100, verbose_name="Región")
    telefono = models.CharField(max_length=20, blank=True, verbose_name="Teléfono")
    fecha_apertura = models.DateField(null=True, blank=True, verbose_name="Fecha de Apertura")
    activa = models.BooleanField(default=True, verbose_name="Activa")

    def __str__(self):
        return f"{self.nombre} - {self.comuna}"