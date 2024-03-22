"""
Pedimos al usuario un carácter a codificar.
"""

caracter = input("Introduzca el carácter a codificar con or exclusivo o XOR: ")

"""
Vamos a ingresar la clave con la que codificaremos.
"""

clave = input("Introduzca el carácter con el que codificará el primero: ")

"""
Mostramos el resultado de codificar
"""

criptograma = chr(ord(caracter) ^ ord(clave))

print ("El carácter codificado es: " + criptograma)

