# Ejemplo de lectura de fichero
# del libro Introducción a la programacióin con python 3
# de Andrés Marzal et al.

# Aseguramos que el fichero existe y tenemos acceso
try:
  # Abrimos el fichero
  fichero = open('ejemplo.txt', 'r')

  # Realizamos operación de lectura/escritura
  for línea in fichero:

    # Si hay un '/n' al final de la línea, lo eliminamos
    if línea[-1] == '\n':
      línea = línea[:-1]
      
    print(línea)
    
  # Cerramos fichero
  fichero.close()

except IOError:
  print('No se puede acceder al fichero.')
