def letra_dni(dni):
  soporte = 'TRWAGMYFPDXBNJZSQVHLCKE'
  # obtengo la posición en el string de soporte y retorno la letra del string en esa posición.
  return soporte[ dni % 23 ]

num_dni = 33661222
print('Según DNI generator el dni '+ str(num_dni) + ' tiene por letra D.')
print('Nuestra función dice que tiene la letra ' + letra_dni(num_dni))
