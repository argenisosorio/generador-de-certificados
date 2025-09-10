# 📄 Generador masivo de Certificados en PDF

Herramienta para generar certificados en formato PDF de manera masiva a partir de una lista de participantes, utilizando una plantilla personalizable en formato SVG.

## ✅ Características

- Generación masiva de certificados en PDF.
- Plantilla personalizable en formato SVG.
- Soporte para múltiples roles.
- Entrada de datos mediante archivo CSV.

## ✅ Requisitos previos

- Python 3.6 o superior.
- Inkscape (para conversión SVG a PDF).
- Sistema operativo: Probado en Linux.

## ✅ Instalación

Ubuntu/Debian

### 1. Instalar Inkscape

```
$ sudo apt update

$ sudo apt install inkscape
```

### 2. Clonar o descargar el proyecto

```
$ sudo apt install git

$ git clone https://github.com/argenisosorio/generador-de-certificados

$ cd generador-de-certificados
```

## ✅ Estructura del Proyecto

```
generador-de-certificados/
│
├── certificado.py                # Script principal.
├── README.md                     # Documentación del proyecto.
├── LICENSE                       # Licencia del Software.
└── utils/                        # Directorio con archivos que usa el script.
    ├── certificado.svg           # Plantilla SVG del certificado.
    └── participantes.csv         # Archivo CSV con datos de ejemplo.
```

## ✅ Formato del Archivo CSV

El archivo CSV debe seguir esta estructura:

```
nombre,cedula,rol
María González,12345678,0
Juan Pérez,87654321,1
Carlos Rodríguez,56781234,2
```

## ✅ Códigos de Roles

```
Código | Rol
0	Profesor
1	Estudiante
2	Facilitador
3	Asistente
4	Ponente
5	Organizador
6	Colaborador
```

## ✅ Uso Rápido

### Generar certificados:

```
$ python3 certificado.py
```

### Encontrar los certificados:

Los PDFs generados se guardarán en la carpeta raíz del proyecto, el nombre de la carpeta será el nombre que se introdujo por pantalla durante la ejecución del script.

## ✅ Personalización

- Modificar lista de participantes: Edite el archivo participantes.csv agregando los datos de los participantes así como su respectivo rol, manteniendo la estructura del archivo.

- Modificar la Plantilla: Edite el archivo utils/certificado.svg con Inkscape o cualquier editor de SVG, mantenga los marcadores de posición {nombre}, {cedula}, {rol}, personalice colores, logos y diseño general

## ✅ Licencia

Este proyecto está bajo la Licencia GNU GENERAL PUBLIC LICENSE Version 2. Vea el archivo LICENSE para más detalles.

## ✅ Créditos

Basado en el trabajo original de David Hernández [Generador en masa de certificados en pdf de David Hernández](https://github.com/davidhdz/generador-de-certificados)

## ✅ Soporte

Para soporte técnico abra un issue en el repositorio de GitHub o escriba al correo argenisosorio10@gmail.com

-----

⭐ ¡Dé una estrella al proyecto si le resulta útil!
