#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Generador de certificados pdf usando una plantilla svg a través de inkscape
# Copyright 2016 David Hernández

# certificado.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# certificado.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with certificado.py. If not, see <http://www.gnu.org/licenses/>.

# Modificaciones del Ing. Argenis Osorio (argenisosorio10@gmail.com).

import os
import csv
import time
import sys
import traceback
from subprocess import Popen

def generar(reemplazos, nombre, cedula, rol, contador, siglas_evento):
    """
    Genera el certificado en formato pdf.
    """
    tiempo = str(int(time.time()))  # Para el nombre temporal
    nombretmp = '/tmp/' + tiempo + str(contador) + '.certificado.svg'  # Nombre único temporal del svg modificado
    with open('../utils/certificado.svg', 'r') as entrada, open(nombretmp, 'w') as salida:
        for line in entrada:  # Reemplazo de variables en el archivo svg
            for src, target in reemplazos.items():
                line = line.replace(src, target)
            salida.write(line)
    certsalida = cedula + '-' + siglas_evento + "-" + rol + '.pdf'  # Nombre del certificado pdf final
    print("-" + str(contador) + " Generando certificado" " para " + nombre)
    x = Popen(['/usr/bin/inkscape', nombretmp, '-o', certsalida])  # Generación del certificado temporal.
    x.wait()  # Esperar a que Inkscape termine antes de continuar
    print("\n-Removiendo archivos temporales...\n")
    time.sleep(5)
    if os.path.exists(nombretmp):
        x = Popen(['rm', nombretmp])  # Eliminación de archivos temporales
    os.chdir("..")  # Retrocediento un directorio para conseguir a la carpeta utils

print("\n** Generador de certificados pdf usando una plantilla svg a través de inkscape **\n")
evento = input("Escriba el nombre del evento/curso, ejemplo: Foro de Seguridad Informática: ")
siglas_evento = input("Escriba las siglas del evento/curso, más el mes y el año separado por guión, ejemplo: fsi-09-18: ")

def main():
    """
    Función que recolecta los datos y los envía a la función de generación.
    """
    if not os.path.exists(siglas_evento):
        os.makedirs(siglas_evento)
    try:
        contador = 0
        contador2 = 1
        with open('utils/participantes.csv', 'r') as listado:
            datos = csv.reader(listado, delimiter=',')
            for row in datos:
                if row[0].startswith('#'):
                    continue
                nombre = row[0]
                cedula = row[1]
                if row[2] == '0':
                    rol = 'Profesor'
                if row[2] == '1':
                    rol = 'Estudiante'
                if row[2] == '2':
                    rol = 'Facilitador'
                if row[2] == '3':
                    rol = 'Asistente'
                if row[2] == '4':
                    rol = 'Ponente'
                if row[2] == '5':
                    rol = 'Organizador'
                if row[2] == '6':
                    rol = 'Colaborador'
                reemplazos = {'nombre_del_participante': nombre, 'cedula': cedula, 'Rol': rol}
                contador = contador + 1
                os.chdir(siglas_evento)

                with open('data_final.csv', 'a', newline='') as myfile:
                    wr = csv.writer(myfile, escapechar=' ', quoting=csv.QUOTE_NONE)
                    wr.writerow([nombre, cedula, evento, rol, siglas_evento + '/' + cedula + '-' + siglas_evento + "-" + rol + '.pdf'])

                generar(reemplazos, nombre, cedula, rol, contador, siglas_evento)  # Función de generación de certificados

        listado.close()
        print("\n----------\n")
        print("¡Finalizó el proceso! Total de certificados generados: " + str(contador) + "\n")
    except KeyboardInterrupt:
        print("Interrupción por teclado.")
    except Exception as e:
        print("Error general:", e)
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)

if __name__ == "__main__":
    main()
