**INFORMACION DEL PROYECTO**

* Nombre completo del proyecto: *CRUD Products*
* Número de proyecto: *1*
* Version de Mongo DB: *5.0.14*

---

#### TABLA DE CONTENIDOS:
---

- [IMPORTANTE](#IMPORTANTE)
- [COMANDOS USADOS](#COMANDOS-USADOS)

---

#### IMPORTANTE

2. Debemos tener instalado "pip 3" de "python 3", de acuerdo al sistema
   operativo donde nos encontremos

3. Debemos tener instalado "virtualenv" de "python 3", de acuerdo al sistema
   operativo donde nos encontremos

4. Para iniciar nuestro proyecto ejecutamos los comandos de la seccion
   **[COMANDOS USADOS](#COMANDOS-USADOS)**, no agregamos la carpeta de "Virtualenv", porque pesa
   mucho y no tiene sentido agregarla ya que solo es para el desarrollo
   de nuestro proyecto

5. Antes de correr el proyecto debemos correr el script de nuestra base
   de datos en Mysql o MariaDB											

6. Si usamos MariaDB, en la seccion del host usar 127.0.0.1
   no localhost, ya que da errores, si la base de datos es Mysql no
   da ningun problema

*En el caso que exista dudas sobre el proyecto ver el siguiente tutorial: [PyMongo, Python & Mongodb - #1](https://youtu.be/QRu2B0xQf04)*

---

#### COMANDOS USADOS

1. Los siguientes comandos los vamos a ejecutar dentro de la carpeta de
   nuestro proyecto

2. Primero vamos crear una maquina virtual de Python 3 usando "virtualenv"
   con la finalidad de instalar los modulos de nuestro proyecto unicamente
   en esa maquina virtual y no en nuestro sistema, evitando asi que exista
   errores en nuestro sistema con los modulos de Python que instalemos
   
```
virtualenv venv
```

3. Iniciamos la maquina virtual que hemos creado, dependiendo del sistema
   operativo en que nos encontremos

* *Para sistemas operativos Windows*

```
.\venv\Scripts\activate
```

* *Para sistemas operativos Mac y GNU/Linux*

```
source ./venv/bin/activate
```

4. Si no deseamos instalar modulo a modulo podemos ejecutar el siguiente
   comando para instalar todos los módulos necesarios para nuestro proyecto

   **-r** = *esto nos permite dar una ruta en donde se encuentra nuestro archivo 
	    **requirements.txt**, si no ponemos esto nos dara un error*

```
pip install -r requirements.txt 
```

5. Instalamos el módulo del framework de Flask

```
pip install flask
```

6. Instamos el conector de Flask a Mysql

```
pip install flask-mysqldb
```


7. Iniciamos nuestra aplicación

```
python src/app.py
```

8. Ahora si deseamos istar todos los requerimientos que nuestra aplicacion necesita para desplegarse, debemos estar dentro de Virtualenv y ejecutar el siguiente comando, para que nos liste todos los modulos necesarios que nuestra aplicacion necesita, esto es recomendable realizarlos ya que algunos paquetes de Python son incompatibles con la programación de nuestro código

```
pip freeze
```

* *Dentro de nuestro proyecto vamos a crear el archivo de requirements.txt, donde vamos a copiar todos los requerimientos que el comando anterior ha desplegado, lo vamos a crear en el directorio raiz del proyecto*

```
requirements.txt
```
