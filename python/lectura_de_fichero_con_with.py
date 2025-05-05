"""
Ejemplo de lectura de fichero
del libro Introducción a la programacióin con python 3
de Andrés Marzal et al.

DATE: 05 May 2025

WHY: 
El libro del curso no hace referencia a la sistaxis de with, que aunque lleva algún tiempo 
en python ha ido variando su semántica en distintas versiones.
Aquí reescribo el ejemplo homónimo para ver cómo quedaría con la sentencia y doy una 
pequeña referencia a la documentación oficial, que explica en detalle qué implica el uso
de la sentencia para la versión 3.13 de Python.

REFERENCE: https://docs.python.org/es/3.13/reference/compound_stmts.html#the-with-statement
"""

# Aseguramos que el fichero existe y tenemos acceso
try:
  # Abrimos el fichero
  with open('ejemplo.txt', 'r') as fichero:

    # Realizamos operación de lectura/escritura
    for línea in fichero:

      # Si hay un '/n' al final de la línea, lo eliminamos
      if línea[-1] == '\n':
        línea = línea[:-1]
      
      print(línea)
    
    # Cuando finaliza el bucle with, se llama al métido exit del objeto fichero,
    # que es de clase File y se cierra el archivo, que no es necesario cerrar explícitamente.
  
except IOError:
  print('No se puede acceder al fichero.')
