from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Opciones de género
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]

    
    rut = models.CharField(max_length=12, unique=True, verbose_name="RUT")
    
    nombre_completo = models.CharField(max_length=150, verbose_name="Nombre Completo")

    correo = models.EmailField(unique=True, verbose_name="Correo")

    # 4. Fecha de nacimiento
    fecha_nacimiento = models.DateField(null=True, blank=True, verbose_name="Fecha de Nacimiento")

    # 5. Género (Hombre / Mujer / Otro)
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

class Empleado(models.Model):
    # Relación 1 a 1 con el modelo User
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='empleado_profile')
    
    cargo = models.CharField(max_length=100, verbose_name="Cargo / Puesto")
    salario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Salario")
    fecha_contratacion = models.DateField(auto_now_add=True, verbose_name="Fecha de Contratación")

    def __str__(self):
        return f"Empleado: {self.user.nombre_completo} - {self.cargo}"

