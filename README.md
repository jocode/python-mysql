# Aplicación web con pyhton y mysql

**Instalamos los modulos de flask y mysql**

* Creamos un ambiente virtual. Para eso nos ubicamos en la carpeta del proyecto y usamos el comando

* `virtualenv venv` Para python2

* `python3 -m venv venv` Para python3

Luego iniciamos el ambiente virtual usando el comando

* `source venv/bin/activate`

Creamos una carpeta **lib** donde colocaremos todas las dependencias del proyecto

Esto nos instalará las dependencias en la carpeta **lib**

* `pip3 install flask flask-mysqldb -t lib`

Ìnstala las dependencias que tengamos en el archivo `requirements.txt`

* `pip3 install -r requirements.txt -t lib`

Instala de manera global las dependencias

* `pip3 install flask flask-mysqldb`



## Iniciamos la creación del proyecto 

* Creamos el archivo principal **App.py**


Cada vez que prendamos el computador, tan solo debemos iniciar el servidor virtual y ejecutar el archivo de pyhton 

*Recordar que debemos abrir la terminal en donde tengamos el proyecto para que pueda funcionar. El código de la aplicación está en la carpeta `src`*

* `source venv/bin/activate`

* `cd src`

* `python3 App.py`


**IMPORTANTE**

Hay una página llamada [bootswatch](https://bootswatch.com/) que tiene temas gratuitos de Bootstrap, usando propias personalizaciones 

Otra herramienta útil es el sitio web [uigradients](https://uigradients.com) que permite tener gradientes

> El proyecto no se sube el ambiente virtual (venv) ni las librerías utilizadas (libs). Las librerías necesarias están puestas en el archivo `requirements.txt`. Solo se debe seguir los pasos anteriores para instalar las dependencias e iniciar el entorno virtual.


* `pip freeze` Muestra los paquetes instalados en formato de requerimientos.

* `pip list` Lista de paquetes instalados, incluyendo editables.


Como en nuestro caso creamos el ambiente virtual con python3, por defecto al escribir **python** tendremos las versión 3 del lenguaje.

Podemos probar donde está instalado el ejecutable, mediante el comando 

* `which python` Versión por defecto

* `which python2` Para saber donde está python 2

* `which python` Para saber donde está python 3

Si tenemos instalado el interprete en la carpeta del proyecto, mostrará la ruta donde está nuesto proyecto, de lo contrario si está instalado en todo el computador nos mostrará algo como esto `/usr/bin/python2` indicando que está instalado en todo el sistema

Siendo así y teniendo python3 como defecto podemos ejecutar 

* `pip freeze` Para ver las dependencias que usa nuestro proyecto ó

* `pip install module` Para instalar los modulos requeridos en el ambiente virtual 

**PARA RECORDAR**

Siempre que utilicemos esto, debemos previamente haber iniciado el ambiente virtual con 

* `source venv/bin/activate` Donde **venv** es la carpeta donde hemos creado el ambiente virtual. Nosotros podemos darle el nombre que queramos, pero eso se hace al crear el entorno virtual.

Con el comando 

* `pip freeze > requirements.txt` Nos crea el archivo requerimientos con todas las dependencias necesarias

Luego si lo tenemos, tan solo es ejecutar el siguiente comando que nos instalará los modulos que requiere nuestro proyecto

* `pip install -r requirements.txt` 

*Para más información sobre ambientes virtuales ver el enlace* [Virtual Environments and Packages](https://docs.python.org/3/tutorial/venv.html)

Si hay problemas con pip, podemos desistalarlo y volverlo a instalar usando

- `sudo python3 -m pip uninstall pip && sudo apt install python3-pip --reinstall`