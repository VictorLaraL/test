# Power Plant Test
Django test

**Instalación manual**

1. Requisitos:
Postgres 13.1
Python 3.8.8

2. Crear una base de datos nueva en postgres.

3. Crear un nuevo archivo en `./power_plant/.env` con el contenido del archivo `./power_plant/env.example` y cambiar las variables de base de datos. 

4. En la raíz del proyecto ejecutar el siguiente comando para instalar las dependencias:
`pip install -r requirements.txt`

5. Ejecutar las migraciones: 
`python manage.py migrate`

6. Ejecutar el siguiente comando para iniciar la aplicación:
`python manage.py runserver`

**Extras**

* La documentacion del Swagger esta en el puerto: http://localhost:8000/, ahi dentro estan los endpoints que se solicitaron.

* El diagrama de entidades y relaciones esta en la carpeta raiz como Test.draw.pdf

* El deploy del examen se encuentra en la liga: https://testpowerplant.herokuapp.com/
