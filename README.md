# INTRODUCCION
Resolvi el challenge con Django y Django Rest Framework, lenguaje Python

# INSTRUCCIONES DE INSTALACION
Primero, clonemos el repositorio de GitHub:
```
git clone git@github.com:MiguelSequeiros/tax-payments-provider.git
```
Con docker compose, levantemos el entorno de desarrollo:
```
docker-compose build --no-cache
```
Note usted que la primera vez que lo corra, probablemente tenga que tener permisos de super administrador o sudo
```
sudo docker-compose build --no-cache
```
No debería de arrojar mayor problema.


# CORRIENDO LA APLICACION
Instalado el entorno de desarrollo, podemos correr la aplicación.
Primero levantamos los servicios:
```
docker-compose up -d
```
Luego corremos las migraciones necesarias
```
docker-compose run web python manage.py migrate
```
Y listo, no se agregó una capa de autenticación para reducir complejidad a la aplicación
De cualquier forma, tenemos que crear un super usuario para que pueda probar el admin de django en
localhost:8000/admin/ y también para poder usear la interfaz que ofrece django rest framework
```
docker-compose run web python manage.py createsuperuser
```

# EXPLORANDO LA API
Para explorar la API podemos usar la interfaz que entrega django rest framework por defecto.
Si no cambió ningún parámetro de configuración, los endpoints están expuestos su localhost:8000/api/

# PAYABLES

```
localhost:8000/api/payables/
```
En el caso de la entidad payables, podemos filtrar añadiendole una query string:
?servicio=<id del servicio>

| id | servicio |
|----|----------|
| 0  | Agua     |
| 1  | Luz      |
| 2  | Telefono |
| 3  | Internet |
| 4  | Gas      |

Si no añadimos la query string, nos devolverá las boletas de pago sin pagar

# TRANSACTIONS
```
localhost:8000/api/transactions/
```
En el caso de la entidad transactions, podemos filtrar añadiendole dos query string:
?date_after=<fecha>&date_before=<fecha>

la fecha tiene que poner en formato YYYY-MM-DD

