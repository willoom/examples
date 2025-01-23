"""
AUTOR: Willoom
FECHA: 23 de enero de 2025

Este programa solicita por pantalla tres lados de un triámngulo y 
muestra el perímetro y su área, con las unidades métricas del S.I.

Propuesta a la actividad 38 página 79 del libro
Introducción a la orgramación con Python 3, de la
Universitat Jaume I
ISBN: 978-84-697-1178-1
"""

from math import sqrt

a = float(input('Introduzca el lado 1: '))
b = float(input('Introduzca el lado 2: '))
c = float(input('Introduzca el lado 3: '))

perímetro = a + b + c

s = perímetro / 2

área = sqrt(s * (s-a) * (s-b) * (s-c))

print("Para los lados a={0}, b={1}, c={2}...".format(a,b,c))
print("... el perímetro es {0:.2f} metros.".format(perímetro))
print("... el área es {0:.2f} metros cuadrados.".format(área))
