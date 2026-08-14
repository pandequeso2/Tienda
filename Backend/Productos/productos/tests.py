from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Producto


class ProductoAPITests(APITestCase):
    def setUp(self):
        self.producto = Producto.objects.create(
            nombre="Papas fritas",
            sku="SKU-001",
            precio=2000,
            stock=10,
        )

    def test_listar_productos(self):
        url = reverse('producto-list')
        respuesta = self.client.get(url)
        self.assertEqual(respuesta.status_code, status.HTTP_200_OK)
        self.assertEqual(len(respuesta.data), 1)

    def test_crear_producto(self):
        url = reverse('producto-list')
        datos = {
            "nombre": "Bebida",
            "sku": "SKU-002",
            "precio": "1500.00",
            "stock": 5,
        }
        respuesta = self.client.post(url, datos, format='json')
        self.assertEqual(respuesta.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Producto.objects.count(), 2)

    def test_eliminar_producto(self):
        url = reverse('producto-detail', args=[self.producto.id])
        respuesta = self.client.delete(url)
        self.assertEqual(respuesta.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Producto.objects.count(), 0)