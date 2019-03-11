# Aplicación web con pyhton y mysql

1. Instalamos los modulos de flask y mysql 

* Creamos un ambiente virtual. Para eso nos ubicamos en la carpeta del proyecto y usamos el comando

* `virtualenv venv` Para python2

* `python3 -m venv venv` Para python3

Luego iniciamos el ambiente virtual usando el comando

* `source venv/bin/activate`

Creamos una carpeta **lib** donde colocaremos todas las dependencias del proyecto

Esto nos instalará las dependencias en la carpeta **lib**

* `pip3 install flask-mysqldb -t lib`

Ìnstala las dependencias que tengamos en el archivo `requirements.txt`

* `pip3 install -r requirements.txt -t lib`

Instala de manera global las dependencias

* `pip3 install flask-mysqldb`



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