"""
Pedimos al usuario un carácter codificado.
"""

criptograma = input("Introduzca el carácter codificado con or exclusivo o XOR: ")

"""
Vamos a ingresar la clave con la que codificamos.
"""

clave = input("Introduzca el carácter con el que se codificó: ")

"""
Mostramos el resultado de descodificar
"""

mensaje = chr(ord(criptograma) ^ ord(clave))

print ("El carácter original es: " + mensaje)

