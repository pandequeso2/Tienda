from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User


class UsuarioAPITests(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(
            username="jperez",
            password="ClaveSegura123",
            email="jperez@correo.com",
            rut="12345678-9",
            nombre_completo="Juan Pérez",
            correo="jperez@correo.com",
            tipo_usuario="CLIENTE",
        )

    def test_listar_usuarios(self):
        url = reverse('usuario-list')
        respuesta = self.client.get(url)
        self.assertEqual(respuesta.status_code, status.HTTP_200_OK)
        self.assertEqual(len(respuesta.data), 1)

    def test_crear_usuario(self):
        url = reverse('usuario-list')
        datos = {
            "username": "mgonzalez",
            "password": "OtraClave456",
            "email": "mgonzalez@correo.com",
            "rut": "98765432-1",
            "nombre_completo": "María González",
            "correo": "mgonzalez@correo.com",
            "tipo_usuario": "EMPLEADO",
        }
        respuesta = self.client.post(url, datos, format='json')
        self.assertEqual(respuesta.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

    def test_password_no_se_expone_en_la_respuesta(self):
        url = reverse('usuario-detail', args=[self.usuario.id])
        respuesta = self.client.get(url)
        self.assertNotIn('password', respuesta.data)

    def test_no_permite_rut_duplicado(self):
        url = reverse('usuario-list')
        datos = {
            "username": "otro",
            "password": "Clave789",
            "rut": "12345678-9",  # ya existe en setUp
            "nombre_completo": "Otro Usuario",
            "correo": "otro@correo.com",
        }
        respuesta = self.client.post(url, datos, format='json')
        self.assertEqual(respuesta.status_code, status.HTTP_400_BAD_REQUEST)

    def test_eliminar_usuario(self):
        url = reverse('usuario-detail', args=[self.usuario.id])
        respuesta = self.client.delete(url)
        self.assertEqual(respuesta.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)