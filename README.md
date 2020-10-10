# Practicas Laboratorio Software Avanzado
## Segundo Semestre 2020
## Christopher Lopez 201504100
--------------------------------------------------
### Practica 9

#### LINK VIDEO : https://youtu.be/9Y4YeC36A6k

#### Descripcion del Proyecto
Se cuenta con dos servicios usando contenedores, contruyendolos con
la herramienta Docker compose
- Servicio Web : Servidor Flask que retorna una pagina web con los datos insertados en una Base de Datos.
- Servicio mysql: Servidor de Base de Datos MariaDB con datos que son consultados por el servicio web.

#### Construccion en Docker Compose
Se realizo la construccion de una imagen con un DockerFile
donde se realizaron las siguientes instalaciones definidas en el archivo requeriments.txt
- Libreria Flask para servidores HTTP
- Libreria mysql-connector para poder realizar la conexion python con MariaDB
```dockerfile
FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
```
Archivo requirements.txt
```txt
flask
mysql-connector-python==8.0.11
```
#### Descripcion de Contenedores
**Contenedor : Servicio Web**
- Lenguaje Python 3
- PIP3 para el manejo de paquetes
- Flask para creacion de servicios Web
- Herramienta mysql-connection para realizar conexion a la base de datos MySQL o MariaDB
- **PUERTO: 80**

**Contenedor: Servicio mysql**
- Base de datos MariaDB 8.0.1
- **PUERTO : 3306**

#### Volumnes
- Volumen en Servicio Web para el codigo a ejecutar de la aplicacion
- Volumen de la base de datos para la persistencia de datos llamado **data-volume** definido en el docker-compose
donde el target es /var/lib/mysql
```dockerfile
        volumes:
            - data-volume:/var/lib/mysql
        environment:
            MYSQL_ROOT_PASSWORD: root
            MYSQL_DATABASE: TIENDA
            MYSQL_USER: sapractica
            MYSQL_PASSWORD: sapractica
volumes:
    data-volume:
```
#### Definicion de la Base de Datos
La definicion de la base de datos y los usuarios se realizo en el archivo docker-compose 
- Nombre de la BD: **TIENDA**
- MYSQL_USER: sapractica
- MYSQL_PASSWORD: sapractica

Los datos que se insertan en la BD al levantar los servicios de docker-compose
en la tabla : VIDEOJUEGOS

DATOS INSERTADOS MOSTRADOS ABAJO EN LA PRACTICA 8

--------------------------------------------------
### Practica 8

#### LINK VIDEO: https://youtu.be/aJ306ZaPsas

#### Descripcion del Proyecto
Se cuenta con dos servicios usando contenedores, contruyendolos con
la herramienta Docker compose
- Servicio Web : Servidor Flask que retorna una pagina web con los datos insertados en una Base de Datos.
- Servicio mysql: Servidor de Base de Datos MariaDB con datos que son consultados por el servicio web.

La base de datos tiene almacenado datos de 5 videojuegos donde se muestra el nombre,genero y plataforma en
la que se lanzaron. 

#### Descripcion de Contenedores
**Contenedor : Servicio Web**
- Lenguaje Python 3
- PIP3 para el manejo de paquetes
- Flask para creacion de servicios Web
- Herramienta mysql-connection para realizar conexion a la base de datos MySQL o MariaDB
- **PUERTO: 80**

**Contenedor: Servicio mysql**
- Base de datos MariaDB 8.0.1
- **PUERTO : 3306**


#### Enlaces
Se creo un unico enlace en el servicio Web que se contecta al contenedor de mysql
- "mysql"

#### Volumnes
- Volumen en Servicio Web para el codigo a ejecutar de la aplicacion
- Volumen de la base de datos para la insercion de datos definidios en el archivo **data.sql** en la maquina local

#### Definicion de la Base de Datos
La definicion de la base de datos y los usuarios se realizo en el archivo docker-compose 
- Nombre de la BD: **TIENDA**
- MYSQL_USER: sapractica
- MYSQL_PASSWORD: sapractica

Los datos que se insertan en la BD al levantar los servicios de docker-compose
en la tabla : VIDEOJUEGOS

| ID | Nombre | Genero | Plataforma |
| ------------- | ------------- | ------------- | ------------- |
| 1  | Super Mario Galaxy  | Plataformas | Wii
| 2  | Forza Horizon 4  | Conduccion | Xbox One
| 3  | God of War  | Accion/Aventuras | PS4 |
| 4  | Resident evil 7 | Survival Horror | Multiplataforma |
| 5  | Gears of War 5  | Accion | Xbox One | 

Estos datos se muestran en la pagina **indext.html** que retorna el servicio web al ingresar. 






