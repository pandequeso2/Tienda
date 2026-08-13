Para Probar el Proyecto tienes que

Paso 0: Crear Bases de Datos

Usaurio: usuario_service_db
Empleado: empleado_service_db
Sede: sede_service_db
Producto: producto_service_db

Paso 1: python -m venv venv     

Paso 2: venv\Scripts\activate 

Paso 3: pip install -r ../../requirements.txt

Paso 4: python manage.py migrate

Paso 5: python manage.py runserver 8000


URL:

Gateway:
http://127.0.0.1:8080/api/usuarios/
http://127.0.0.1:8080/api/productos/
http://127.0.0.1:8080/api/empleados/
http://127.0.0.1:8080/api/sedes/


Usuarios: http://localhost:8000/api/usuarios/
Empleados: http://localhost:8000/api/empleados/
Sedes: http://localhost:8000/api/sedes/
Productos: http://localhost:8000/api/productos/