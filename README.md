# Generador en masa de certificados en pdf

Basado en: [Generador en masa de certificados en pdf by David Hernández](https://github.com/davidhdz/generador-de-certificados)

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
Carlos Parra,15796551,3
```
Los valores de la columna Rol que es la tercera pueden ser:

* 0 es Ponente
* 1 es Organizador
* 2 es Asistente

## Paquetes de Python requeridos

pdfmerge

## Probar el generador de certificados
```
$ python certificado.py
```
