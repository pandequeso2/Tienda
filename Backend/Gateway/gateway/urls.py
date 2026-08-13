from django.urls import path, re_path
from .views import proxy_view

urlpatterns = [
    re_path(r'^api/(?P<servicio>\w+)/(?P<ruta>.*)$', proxy_view, name='proxy'),
]