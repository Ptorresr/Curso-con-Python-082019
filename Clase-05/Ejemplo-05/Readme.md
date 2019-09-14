##### EJEMPLO-05
## CRUD DE DATOS CON PYTHON EN MYSQL

### OBJETIVO
Conocer el procedimiento para realizar un CRUD de datos a una tabla en un servidor MariaDB desde Python.

#### REQUISITOS
1. Contar con los datos de conexión a la base de datos Biblioteca.

   __Host:__ localhost
   __User:__ Biblioteca \
   __Password:__ Biblioteca \
   __Base de datos:__ Biblioteca

1. Contar con la tabla __Libro__ creada y con datos muestra en la base de datos:

  ![Tabla Libro](assets/tabla-libro.jpg)

1. Usar la carpeta de trabajo `Clase-05/Ejemplo-04`

   ```sh
   $ cd Clase-05/Ejemplo-05

   Clase-05/Ejemplo-05 $
   ```

1. Instalar el módulo `mysql-connector-python` que será el responsable de permitir realizar una conexión a base de datos MySQL / MariaDB desde Python.

   __Sito principal:__
   https://dev.mysql.com/doc/connector-python/en/

   __Instalación con el comando pip:__
   ```sh
   $ pip install mysql-connector-python
   Collecting mysql-connector-python
   Using cached https://files.pythonhosted.org/packages/43/bd/43a128bbd6a3237d6f255c7afaa9308430d5c90f8db8371276169722f037/mysql_connector_python-8.0.16-cp37-cp37m-manylinux1_x86_64.whl
   Requirement already satisfied: protobuf>=3.0.0 in /home/rctorr/miniconda3/lib/python3.7/site-packages (from mysql-connector-python) (3.7.1)
   Requirement already satisfied: six>=1.9 in /home/rctorr/miniconda3/lib/python3.7/site-packages (from protobuf>=3.0.0->mysql-connector-python) (1.12.0)
   Requirement already satisfied: setuptools in /home/rctorr/miniconda3/lib/python3.7/site-packages (from protobuf>=3.0.0->mysql-connector-python) (41.0.0)
   Installing collected packages: mysql-connector-python
   Successfully installed mysql-connector-python-8.0.16

   $
   ```

### DESARROLLO
1. __OPERACIÓN READ__ Crea el script `lista-registros.py` que imprima en formato texto en la salida estándar la lista de registros de la tabla proporcionada como parámetro en la línea de comandos. Hacer uso de los módulos `click`, `mysql-connector-python` y `stdout`.

   __Caso: Ejecutando el script sin argumentos__

   ```sh
   Clase-05/Ejemplo-05 $ python lista-registros.py

   Tablas disponibles
   ------------------
   Libro
   ------------------
   ```

   __Caso: Imprimiendo registros de la tabla Libro__

   ```sh
   Clase-05/Ejemplo-05 $ python lista-registros.py Libro

   Tabla: Libro
   ------------
   Id | Titulo                 | Editorial   | NumPag | Autores
    1 | Yo, Robot              | Gnome Press |    374 |       1
    2 | El fin de la eternidad | Gnome Press |    191 |       1
    3 | El arte de la guerra   | Obelisco    |    112 |       2
   ------------
   ```
   ***

__Nota:__ En la carpeta ya existe el script `stdout.py` que es un módulo que contiene la función `imprime_registros()` que imprime una lista de registros con un título, se puede consultar la ayuda desde ipython.
