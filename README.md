# Generador en masa de certificados en pdf

Basado en: [Generador en masa de certificados en pdf by David Hernández](https://github.com/davidhdz/generador-de-certificados)

Versión de Python requerida: Python 3.X

## Documentación

1) Descargar el proyecto, nos quedará el fichero comprimido generador-de-certificados-master.zip

2) Lo descomprimimos y nos quedara la carpeta generador-de-certificados que contiene lo siguiente:

- certificado.py, que es el script para generar los certificados.
- La carpeta "utils" que tiene la plantilla .svg del certificado y un fichero .csv que contiene la lista de participantes.

El siguiente es un ejemplo del fichero .csv que contiene los datos de los participantes.
```
#nombre,cedula,rol
José Morales,8035497,0
Karla Perez,16789145,1
Carlos Parra,15796551,2
```
Los valores de la columna Rol que es la tercera pueden ser:

* 0 es Profesor
* 1 es Estudiante
* 2 es Facilitador
* 3 es Asistente
* 4 es Ponente
* 5 es Organizador
* 6 es Colaborador

### Probar el generador de certificados

<b>Nota:</b>
<br />
Usaremos $ para describir los comandos que se usaran con usuario regular.

Usaremos # para describir los comandos que se usaran con superusuario. 

```
# sudo apt install inkscape

$ python certificado.py
```
