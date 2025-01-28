"""
AUTOR: Willoom
FECHA: 27 de enero de 2025

Este programa solicita por pantalla: 
* un capital inicial C en euros
* una tasa de interes i en tanto por ciento y 
* un número n de años

RESTRICCIÓN: 
Antes de calcular el capital final se ha de comprobar que i es positivo.

Muestra cuál será el capital final aplicando el interés compuesto
durante los n años.

Propuesta a la actividad 66 página 102 del libro
Introducción a la orgramación con Python 3, de la
Universitat Jaume I
ISBN: 978-84-697-1178-1
"""

C = float(input('Introduzca el capital inicial: '))
i = float(input('Introduzca el interés en tanto por ciento: '))
n = int(input('Introduzca el número de años de aplicación del interés: '))
if i > 0:
  # Aquí el interés en tanto por uno es mayor que cero, positivo
  print ("Para un capital inicial de {0}€, un interés del {1}% durante {2} años,".format(C,i,n))
  print ("se obtiene un capital final de {0:.2f}€".format(C * (1 + i/100)**n))
else:
  # Aquí el intgerés en tanto pot uno es igual a cero o negativo e imprimimos un mensaje sin calcular nada.
  print ("El capital inicial ha de ser un decimal positivo.")
