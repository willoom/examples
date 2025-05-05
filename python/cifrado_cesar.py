"""

AUTHOR: Willoom
DATE: 05 May 2025

REFERENCE: https://es.wikipedia.org/wiki/Cifrado_C%C3%A9sar

Implementa el siguiente programa para un cifrado César con desplazamiento 
arbitrario.

Lee y escribe carácter a carácter.

Completa el código.

Asumid que el mensaje se codifica sólo con letras en minúsculas.
No codificamos otros caracteres, que se respetarán tal cual, por legibilidad.
"""



archivo_entrada = input('Archivo con mensaje a cifrar:')
archivo_salida = input('Archivo con mensaje cifrado:')

ORD_A = ord('a')
MAX_DESP = ord('z') - ORD_A


desplazamiento_césar = -1
# Mientras no tengamos un valor válido de desplazamiento César, 
while 0 > desplazamiento_césar or desplazamiento_césar > MAX_DESP:
    # pedimos al usuario un desplazamiento válido y aseguramos que sea entero
    try:
        desplazamiento_césar = int(input('Introduzca un desplazamiento válido: '))
    except ValueError:
        print(f'No introdujo un entero entre 0 y {MAX_DESP}.')
try:
    with open(archivo_entrada, 'r') as entrada, open(archivo_salida, 'w') as salida:
        carácter = entrada.read(1)
        while carácter != '':
            
            # Si el carácter está entre la 'a' y la 'z' aplicamos la codificación
            if 'a' <= carácter <= 'z':
                # Tratamos de averiguar el desplazamiento final desde la letra 'a'
                delta = ord(carácter) - ORD_A + desplazamiento_césar
                delta = delta % (MAX_DESP + 1)
                salida.write(chr(ORD_A + delta))
                
            else:
                # En caso de que la letra no sea minúscula entre 'a' y 'z, la respetaremos.
                salida.write(carácter)
            # Leemos el siguiente carácter del fichero
            carácter = entrada.read(1)
except OSError:
    print(f"No se pudo leer {archivo_entrada} o no se pudo escribir {archivo_salida}.")
except:
    print("Otro error.")
    
            
                
      


