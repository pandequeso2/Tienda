from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Empleado


class EmpleadoAPITests(APITestCase):
    def setUp(self):
        self.empleado = Empleado.objects.create(
            user_id=1,
            nombre_empleado="Juan Pérez",
            cargo="Vendedor",
            salario=550000,
        )

    def test_listar_empleados(self):
        url = reverse('empleado-list')
        respuesta = self.client.get(url)
        self.assertEqual(respuesta.status_code, status.HTTP_200_OK)
        self.assertEqual(len(respuesta.data), 1)

    def test_crear_empleado(self):
        url = reverse('empleado-list')
        datos = {
            "user_id": 2,
            "nombre_empleado": "María González",
            "cargo": "Supervisora",
            "salario": "750000.00",
        }
        respuesta = self.client.post(url, datos, format='json')
        self.assertEqual(respuesta.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Empleado.objects.count(), 2)

    def test_no_permite_user_id_duplicado(self):
        url = reverse('empleado-list')
        datos = {
            "user_id": 1,  # ya existe en setUp
            "nombre_empleado": "Otro Empleado",
            "cargo": "Cajero",
            "salario": "500000.00",
        }
        respuesta = self.client.post(url, datos, format='json')
        self.assertEqual(respuesta.status_code, status.HTTP_400_BAD_REQUEST)

    def test_eliminar_empleado(self):
        url = reverse('empleado-detail', args=[self.empleado.id])
        respuesta = self.client.delete(url)
        self.assertEqual(respuesta.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Empleado.objects.count(), 0)