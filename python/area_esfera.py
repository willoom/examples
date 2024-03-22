from math import pi
# Leemos el valor del radio

cad_leída = input('Introduce el radio: ')
radio = float(cad_leída)
volumen = 4/3 * pi * radio ** 3

print("El volumen de una esfera de radio {0:.2f}m es {1:.2f}m cúbicos.".format(radio, volumen))
