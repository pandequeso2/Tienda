from django.db import models

class Empleado(models.Model):
    # No es ForeignKey: el usuario vive en otro microservicio (Tienda/users),
    # así que solo guardamos su ID como referencia.
    user_id = models.PositiveIntegerField(unique=True, verbose_name="ID de Usuario")
    nombre_empleado = models.CharField(max_length=100, blank=True, default='', verbose_name="Nombre de Empleado")

    cargo = models.CharField(max_length=100, verbose_name="Cargo / Puesto")
    salario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Salario")
    fecha_contratacion = models.DateField(auto_now_add=True, verbose_name="Fecha de Contratación")

    def __str__(self):
        return f"Empleado #{self.user_id} - {self.cargo}"