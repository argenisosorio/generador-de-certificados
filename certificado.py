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
import pprint
from subprocess import Popen
import itertools

def generar(reemplazos,nombre,cedula,rol,contador):
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
    certsalida = cedula+'-'+siglas_evento+"-"+rol+'.pdf' # Nombre del certificado pdf final
    print("-" + str(contador) + " Generando certificado"  " para " + nombre)
    x = Popen(['/usr/bin/inkscape', nombretmp, '-o', certsalida]) # Generación del certificado temporal.
    print("\n-Removiendo archivos temporales...\n")
    time.sleep(5)
    x = Popen(['rm', nombretmp]) # Eliminación de archivos temporales
    #x = Popen(['rm', certsalidat]) # Eliminación de archivos temporales    
    os.chdir("..") # Retrocediento un directorio para conseguir a la carpeta utils

print "\n** Generador de certificados pdf usando una plantilla svg a través de inkscape **\n"
evento = raw_input ("Escriba el nombre del evento/curso, ejemplo: Foro de Seguridad Informática: ")
siglas_evento = raw_input ("Escriba las siglas del evento/curso, más el mes y el año separado por guión, ejemplo: fsi-09-18: ")
#rol = raw_input ("Escriba el rol de los participantes: ")

def main():
    """
    Función que recolecta los datos y los envía a la función de generación.
    """
    #siglas_evento = raw_input ("Nombre de la carpeta donde se van a guardar los certificados: ")
    if not os.path.exists(siglas_evento):
        os.makedirs(siglas_evento)
    try:
        contador = 0
        contador2 = 1
        with open('utils/participantes.csv', 'r') as listado: # Lectura de participantes desde un .csv
            datos = csv.reader(listado, delimiter=',') # Separar la data por coma.
            #datos = csv.reader(listado, delimiter=';') # Separar la data por punto y coma.
            alist = [];
            for row in datos:
                if row[0].startswith('#'): # Permite comentar líneas en el archivo csv.
                    continue
                #alist.append(contador2) # Valor que va a tener el campo id del data_final.csv
                nombre = row[0] # Columna 1 que corresponde a Nombre y Apellido.
                alist.append(nombre) # Agregando el valor de nombre a una lista.
                cedula = row[1] # Columna 2 que corresponde a las cédulas de identidad.
                #print row[2]
                #rol = 'Asistente'
                if row[2]=='0': # Columna 3 corresponde a un código de participación
                    rol = 'Profesor'
                if row[2]=='1':
                    rol = 'Estudiante'
                if row[2]=='2':
                    rol = 'Facilitador'
                if row[2]=='3':
                    rol = 'Asistente'
                if row[2]=='4':
                    rol = 'Ponente'
                if row[2]=='5':
                    rol = 'Organizador'
                if row[2]=='6':
                    rol = 'Colaborador'
                alist.append(cedula) # Agregando el valor de cédula a una lista.
                #alist.append(evento) # Agregando el valor del evento.
                alist.append(rol+'\n') # Agregando el valor del evento.
                #alist.append(siglas_evento+"/"+cedula+"-"+siglas_evento+"-"+rol+".pdf") # Agregando el nombre del fichero generado.
                #alist.append(0)
                #alist.append('\n') # Agregando esta cadena para luega hacer el salto de línea.
                contador2 = contador2 + 1

                # Variables de sustitución: nombre, cédula.
                reemplazos = {'nombre_del_participante':nombre, 'cedula':cedula, 'Rol':rol,}
                contador = contador + 1 # Contador que se agrega al nombre temporal del svg
                os.chdir(siglas_evento) # Navegando hasta el directorio donde se van a guardar los certificados
                mylist = alist
                #print mylist
                # Ahora vamos a crear/escribir en data_final.csv los datos de la lista alist.
                with open('data_final.csv', 'wb') as myfile:
                    wr = csv.writer(myfile, escapechar=' ', quoting=csv.QUOTE_NONE)
                    wr.writerow(alist)
                generar(reemplazos,nombre,cedula,rol,contador)  #Función de generación de certificados
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
