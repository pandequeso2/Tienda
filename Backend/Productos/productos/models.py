from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre")
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    sku = models.CharField(max_length=50, unique=True, verbose_name="SKU / Código")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    stock = models.PositiveIntegerField(default=0, verbose_name="Stock")

    # No es ForeignKey: la sede vive en otro microservicio, guardamos solo su ID.
    sede_id = models.PositiveIntegerField(null=True, blank=True, verbose_name="ID de Sede")

    activo = models.BooleanField(default=True, verbose_name="Activo")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    def __str__(self):
        return f"{self.nombre} ({self.sku})"