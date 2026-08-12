from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]

    rut = models.CharField(max_length=12, unique=True, verbose_name="RUT")
    nombre_completo = models.CharField(max_length=150, verbose_name="Nombre Completo")
    correo = models.EmailField(unique=True, verbose_name="Correo")
    fecha_nacimiento = models.DateField(null=True, blank=True, verbose_name="Fecha de Nacimiento")
    genero = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        null=True,
        blank=True,
        verbose_name="Género"
    )

    USER_TYPE_CHOICES = [
        ('CLIENTE', 'Cliente'),
        ('EMPLEADO', 'Empleado'),
        ('ADMIN', 'Administrador'),
    ]

    tipo_usuario = models.CharField(
        max_length=10,
        choices=USER_TYPE_CHOICES,
        default='CLIENTE',
        verbose_name="Tipo de Usuario"
    )

    def __str__(self):
        return f"{self.nombre_completo} ({self.rut})"