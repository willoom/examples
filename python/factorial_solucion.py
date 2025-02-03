"""
AUTOR: Willoom
FECHA: 3 de febrero de 2025

Crea una función llamada factorial que reciba un número.

Aplica recursividad para obtener el valor factorial.

Identifica el caso base teniendo en cuenta que el parámetro formal será mayor que cero.

Imprime por pantalla los mensajes.

El factorial de 3 es 6.
El factorial de 5 es 120.

Invocando a la función.
"""

# recibe un número entero mayor de cero y devuelve su factorial
def factorial(num):
    if num == 1:
        # En el caso base, el más sencillo num es 1 y devolvemos 1
        return 1
    else:
        # En el caso recursivo, el factorial es num por el factorial de num menos uno
        return num*factorial(num-1)
        
def prueba_factorial(num):
    # Aseguramos que hacemos una llamada correcta a factorial
    if num < 1:
        # Éste seria un caso con argumento no válido.
        print("No podemos calcular el factorial de",num)
    else:
        # El argumento está en el rango permitido
        print("El factorial de {0} es {1}.".format(num, factorial(num)))
        
prueba_factorial(3)
prueba_factorial(5)
