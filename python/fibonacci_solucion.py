"""
AUTOR: Willoom
FECHA: 3 de febrero de 2025

Crea una función llamada fibonacci.

Los números de Fibonacci siguen la secuencia 
1,1,2,3,5,8,13,21,34,55...

Imprime por pantalla

El término 4 de Fibonacci es 3.
El término 7 de Fibonacci es XXX.
El término 50 de Fibonacci es XXX.

Donde XXX es el valor calculado por vuestra función.

Usa recursividad.
"""

# recibe un número entero mayor de cero y devuelve su factorial
def fibonacci(num):
    if num == 1 or num == 2:
        # En el caso base, el más sencillo num es 1 y devolvemos 1
        return 1
    else:
        # En el caso inductivo, el factorial es num por el factorial de num menos uno
        return fibonacci(num-1) + fibonacci(num-2)
        
def prueba_fibonacci(num):
    # Aseguramos que hacemos una llamada correcta a factorial
    if num < 1:
        # Éste seria un caso con argumento no válido.
        print("No podemos calcular el tçermino {0} de Fibonacci.".format(num))
    else:
        # El argumento está en el rango permitido
        print("El término {0} de Fibonacci es {1}.".format(num, fibonacci(num)))
        
prueba_fibonacci(4)
prueba_fibonacci(7)
prueba_fibonacci(40)
prueba_fibonacci(45)
