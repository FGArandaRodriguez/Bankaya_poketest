# Bankaya_poketest
<<<<<<< HEAD
Este proyecto consiste de microservicios adaptados al test  de backend

## Requerimientos

Para correr este proyecto es necesario lo siguiente: 

### Instalar Python
Se requiere tener instalada alguna versión de python ( 3.8 o superior).
se puede descargar e instalar siguiendo los pasos desde la pagina oficial www.python.org

Una vez instalado python al ser una versi{on 3, todo lo que ejecutemos será con python3.

### Instalar PIP
Ahora, requerimos tener instalado el instalador de paquetes de python, (pip), en este caso pip3. 
Para ello ejecutaremos el siguiente comando ( en mi caso uso linux): 

```
    sudo apt-get install python3-pip
```

una vez instalado pip, necesitaremos crear un entorno virtual, por lo que procederemos a instalar virtual env, que es una herramienta que nos ayudará a crear el entorno virtual. 
haremos uso de pip para la instalación 

```
sudo pip3 install virtualenv
```

una vez instalado virtual env, procederemos a crear un entorno virtual, para ello ejecutaremos el siguiente comando: 

```
python3 -m venv .venv

```
En este caso yo instalaré el entorno virtual en el directorio raíz del proyecto. 

una vez creado el entorno virtual, será necesario acceder a el y activarlo, esto lo haremos con el comando: 

```
source .venv/bin/activate

```

una vez dentro y activado el entorno virtual, aparecerá al inicio de la línea de comandos de la siguiente forma: (venv)

Ahora, será necesario instalar los requerimientos para poder correr el proyecto. 

Para ello, dentro del entorno virtual ejecutarémos el siguiente comando: 

```
pip3 instal -r requirements.txt

```
Este comando nos ayudará a instalar todas las librerías/bibliotecas necesarias para que nuestro proyecto funcione. 

Una vez instaladas las librerías ya podrémos correr nuestro proyecto, lo harémos con el siguiente comando: 

```
python3 API.py

```
Esto ejecutará el programa y ya podrémos disfrutar de los microservicios aquí contenidos, consumiendolos, ya sea desde el navegador o desde algún cliente de peticiones HTTP tal como postman, insomnia etc.

### Servicios:

A continuación se enlistan los servicios contenidos en este proyecto.
Cabe resaltar que el proyecto corre en el puerto 9000 por defecto, por lo que cuando se inicie de manera local, se podrá acceder con http://localhost:9000/

*NOTA: EL PARÁMETRO <String:name> deberá ser sustituído por el nombre del pokemon.*
*NOTA: TODOS LOS SERVICIOS SON CONSUMIBLES A TRAVÉS DEL MÉTODO (VERBO) GET*

#### Servicio de Bienvenida:

*Este servicio nos dará la bienvenida al poketest*
```
http://localhost:9000/
```

#### Servicio de Datos Requeridos en el Challenge: 

*Este servicio, muestra los datos ordenados | requeridos en el challenge de Bankaya*
```
http://localhost:9000/api/bankaya/pokemon/<string:name>

```

#### Servicio de habilidades:

*Este servicio obtiene las habilidades del pokemon*
```
http://localhost:9000/api/bankaya/pokemon/<string:name>/abilities
```
#### Servicio de nivel de experiencia:
*Este servicio muestra los datos a cerca de la experiencia (exp) de un pokemon*
```
http://localhost:9000/api/bankaya/pokemon/<string:name>/experience
```
#### Servicio de held-items:
*Este servicio obtiene los held-items del pokemon*
```
http://localhost:9000/api/bankaya/pokemon/<string:name>/held-items

```

#### Servicio de ID:
*Este servicio obtiene el ID del pokemon*

```
http://localhost:9000/api/bankaya/pokemon/<string:name>/id
```

#### Servicio de Nombre:
*Este servicio obtiene el nombre del pokemon,en este servicio, podemos buscar por nombre o por ID del pokemon*
```
http://localhost:9000/api/bankaya/pokemon/<string:name>/name
```
#### Servicio de Location-area:
*Este servicio obtiene las locaciones donde se encuentran los pokemon*
```
http://localhost:9000/api/bankaya/pokemon/<string:name>/location-area'

```

# EXTRA BONUS | SERVICIOS EXTRA:

#### Servicio calculo de POW():

*Este servicio calcula la función POW(), manualmente, tal como se pide en el Challenge*

*NOTA: LA BASE ES EL NÚMERO QUE SE QUIERE ELEVAR A LA POTENCIA, Y EL EXPONENTE VENDRÍA SIENDO EL NÚMERO DE LA POTENCIA*
```
http://localhost:9000/POW/<int:base>/<int:exponente>'
```

#### Servicio Visualizador de LOGS en base de datos:

*Este servicio surge a razón que se están guardando datos en una BD SQLite, por lo que para facilitar el trabajo de consultar, solo se debe consumir este api para saber lo que hay en la tabla de logs*

*NOTA: PODEMOS ELIMINAR LA DB QUE VIENE AHÍ PARA QUE AL CONSUMIR CUALQUIER SERVICIO SE CREE UNA NUEVA Y EMPIECE A GUARDAR NUEVOS DATOS*

```
http://localhost:9000/api/bankaya/database/show-data'
```
=======
Este proyecto consiste de microservicios adaptados al test  de backend.
>>>>>>> efe790654f2e126ff19defcd74b2208581ba7347
