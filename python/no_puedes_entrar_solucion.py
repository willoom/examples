"""
AUTOR: Willoom
FECHA: 27 de enero de 2025

Deseamos hacer un programa que gestione la entrada a una discoteca.

Al usuario se le solicita el año en que nació.
El programa calacula su edad y en función de eso, imprime alguno de los siguientes mensajes.

Si el usuario tiene menos de dieciocho años ha de decir, "Lo siento, no tienes la edad suficiente".

Si el usuario, siendo mayor de edad, tiene más de cincuenta, entonces deberá decir: "El bingo es en la sala de abajo".

Si tiene más de 70 debería mostrar por pantalla que "¿No es la hora de tu medicación?".

En otro caso mostrará "Bienvenido, puedes pasar".

RESTRICCIÓN: Comprueba que el usuario no puede introducir valores incorrectos como año de nacimiento.

"""

from datetime import date

# Calculamos el año actual, quedándonos con el campo year de la fecha de hoy
año_actual = date.today().year

# Mostramos el año actual a wfectos informativos.
print("Estamos en el año {0}.".format(año_actual))

# El sistema sólo solicita el año, por lo que a efectos prácticos todos los visitantes
# de la discoteca tendrán el mismo tratamiento que si hubiesen nacido el uno de enero.
año_de_nacimiento = int(input("Introduce el año en el que naciste: "))

edad = año_actual - año_de_nacimiento

# Comprobamos que el cliente no ha nacido en el futuro ni antes de Cristo.
if edad <= 0 or año_de_nacimiento < 0:
  print("No engañas a nadie con esta fecha de nacimiento")
elif edad < 18: # en este punto sabemos que la edad es correcta y positiva...
  # ... es un menor
  print("Lo siento, no tienes la edad suficiente")
elif edad <= 50:
  # ... aquí tiene menos de 51
  print("Bienvenido, puedes pasar")
elif edad <= 70:
  # ... aquí apenas llega a septuagenario pero tiene más de 50
  print("El bingo es en la sala de abajo")
else:
  print("¿No es la hora de tu medicación?")
  

