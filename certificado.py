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

import os
import csv
import time
import sys
import traceback
import pdfmerge
from subprocess import Popen

def generar(reemplazos,nombre,cedula,contador):
    """
    Genera el certificado en formato pdf.
    """
    tiempo = str(int(time.time())) # Para el nombre temporal
    nombretmp = '/tmp/' + tiempo + str(contador) + '.certificado.svg' # Nombre único temporal del svg modificado
    with open('../utils/certificado.svg', 'r') as entrada, open(nombretmp, 'w') as salida:
        for line in entrada: # Reemplazo de variables en el archivo svg
            for src, target in reemplazos.iteritems():
                line = line.replace(src, target)
            salida.write(line)
    entrada.close()
    salida.close()
    certsalidat = '/tmp/'+cedula+'-''.pdf' # Nombre de pdf temporal
    certsalida = cedula+'-'+evento+'-''.pdf' # Nombre del certificado pdf final
    print("-" + str(contador) + " Generando certificado"  " para " + nombre)
    x = Popen(['/usr/bin/inkscape', nombretmp, '-A', certsalida]) # Generación del certificado temporal.
    print("\n-Removiendo archivos temporales...\n")
    time.sleep(5)
    x = Popen(['rm', nombretmp]) # Eliminación de archivos temporales
    #x = Popen(['rm', certsalidat]) # Eliminación de archivos temporales    
    os.chdir("..") # Retrocediento un directorio para conseguir a la carpeta utils

print "\n** Generador de certificados pdf usando una plantilla svg a través de inkscape **\n"
evento = raw_input ("Siglas del evento/curso: ")

def main():
    """
    Función que recolecta los datos y los envía a la función de generación.
    """
    folder = raw_input ("Nombre de la carpeta donde se van a guardar los certificados: ")
    if not os.path.exists(folder):
        os.makedirs(folder)
    try:
        contador = 0
        with open('utils/participantes.csv', 'r') as listado: #Lectura de participantes
            datos = csv.reader(listado, delimiter=',')
            for row in datos:
                if row[0].startswith('#'): # Permite comentar líneas en el archivo csv.
                    continue
                nombre = row[0] # Columna 1 que corresponde a Nombre y Apellido.
                cedula = row[1] # Columna 2 que corresponde a las cédulas de identidad.
                # Variables de sustitución: nombre, cédula.
                reemplazos = {'nombre_del_participante':nombre, 'cedula':cedula,}
                contador = contador + 1 # Contador que se agrega al nombre temporal del svg
                os.chdir(folder) # Navegando hasta el directorio donde se van a guardar los certificados
                generar(reemplazos,nombre,cedula,contador)  #Función de generación de certificados
        listado.close()
        print("\n----------\n")
        print("¡Finalizó el proceso! Total de certificados generados: " + str(contador) + "\n")
    except KeyboardInterrupt:
        print "Interrupción por teclado."
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)

if __name__ == "__main__":
    main()
