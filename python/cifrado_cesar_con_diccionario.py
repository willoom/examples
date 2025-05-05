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

Esta implementación usa un diccionario como base.
Si no existe alguna clave (minúscula) del diccionario, entonces escribimos el carácter 
sin codificar en el fichero de salida.
"""



archivo_entrada = input('Archivo con mensaje a cifrar:')
archivo_salida = input('Archivo con mensaje cifrado:')

ORD_A = ord('a')
MAX_DESP = ord('z') - ORD_A
NUM_VOCALES = MAX_DESP + 1


desplazamiento_césar = -1
# Mientras no tengamos un valor válido de desplazamiento César, 
while 0 > desplazamiento_césar or desplazamiento_césar > MAX_DESP:
    # pedimos al usuario un desplazamiento válido y aseguramos que sea entero
    try:
        desplazamiento_césar = int(input('Introduzca un desplazamiento válido: '))
    except ValueError:
        print(f'No introdujo un entero entre 0 y {MAX_DESP}.')
        
# Aquí ya tenemos los nombres de los ficheros de entrada y salida y el desplazamiento 
# a aplicar.

# Ahora crearemos un diccionario con claves las minúsculas y valor su equivalente codificado.
traductor = dict()
for i in range(NUM_VOCALES):
    traductor[chr(ORD_A+i)] = chr(ORD_A + ((i + desplazamiento_césar) % NUM_VOCALES)) 
    
# No vamos a cambiar el diccionario, por tanto sus claves tampoco variarán.
KEYS = traductor.keys()       

try:
    with open(archivo_entrada, 'r') as entrada, open(archivo_salida, 'w') as salida:
        carácter = entrada.read(1)
        while carácter != '':
            # Si el carácter está en el diccionario, lo traduzco.
            if carácter in KEYS:
                salida.write(traductor[carácter])
            else:
                salida.write(carácter)
            # Tratamos de leer el carácter siguiente.
            carácter = entrada.read(1)
            
except OSError:
    print(f"No se pudo leer {archivo_entrada} o no se pudo escribir {archivo_salida}.")
except:
    print("Otro error.")
    
            
                
      


