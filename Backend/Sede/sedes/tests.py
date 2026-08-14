from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Sede


class SedeAPITests(APITestCase):
    def setUp(self):
        self.sede = Sede.objects.create(
            nombre="Sede Centro",
            direccion="Av. Principal 123",
            comuna="Santiago",
            region="Metropolitana",
            telefono="+56912345678",
        )

    def test_listar_sedes(self):
        url = reverse('sede-list')
        respuesta = self.client.get(url)
        self.assertEqual(respuesta.status_code, status.HTTP_200_OK)
        self.assertEqual(len(respuesta.data), 1)

    def test_crear_sede(self):
        url = reverse('sede-list')
        datos = {
            "nombre": "Sede Norte",
            "direccion": "Calle Falsa 456",
            "comuna": "Antofagasta",
            "region": "Antofagasta",
            "telefono": "+56987654321",
            "activa": True,
        }
        respuesta = self.client.post(url, datos, format='json')
        self.assertEqual(respuesta.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Sede.objects.count(), 2)

    def test_editar_sede(self):
        url = reverse('sede-detail', args=[self.sede.id])
        datos = {"activa": False}
        respuesta = self.client.patch(url, datos, format='json')
        self.assertEqual(respuesta.status_code, status.HTTP_200_OK)
        self.sede.refresh_from_db()
        self.assertFalse(self.sede.activa)

    def test_eliminar_sede(self):
        url = reverse('sede-detail', args=[self.sede.id])
        respuesta = self.client.delete(url)
        self.assertEqual(respuesta.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Sede.objects.count(), 0)