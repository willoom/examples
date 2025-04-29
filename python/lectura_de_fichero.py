# Ejemplo de lectura de fichero

# Aseguramos que el fichero existe y tenemos acceso
try:
  # Abrimos el fichero
  fichero = open('ejemplo.txt', 'r')

  # Realizamos operación de lectura/escritura
  for línea in fichero:
    print(línea)
    
  # Cerramos fichero
  fichero.close()

except IOError:
  print('No se puede acceder al fichero.')
