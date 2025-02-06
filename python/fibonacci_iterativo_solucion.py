"""
AUTOR: Willoom
FECHA: 3 de febrero de 2025

Crea una función llamada fibonacci.

Los números de Fibonacci siguen la secuencia 
1,1,2,3,5,8,13,21,34,55...

Imprime por pantalla al menos:

El término 4 de Fibonacci es 3.
El término 7 de Fibonacci es XXX.
El término 40 de Fibonacci es XXX.

Donde XXX es el valor calculado por vuestra función.

Usa un bucle while.
"""

# recibe un número entero mayor de cero y devuelve término Fibonacci
def fibonacci(num):
    
    if num == 1 or num == 2:
        # En el caso base, el más sencillo num es 1 y devolvemos 1
        return 1
    else:
        i = 3
        i_menos_1 = 1
        i_menos_2 = 1
        # en caso de que nos interese del cuarto término en adelante se entrará en el while
        while i < num:
            i_actual = i_menos_1 + i_menos_2
            i_menos_2 = i_menos_1
            i_menos_1 = i_actual
            i += 1 
        return i_menos_1 + i_menos_2
        
def prueba_fibonacci(num):
    # Aseguramos que hacemos una llamada correcta a factorial
    if num < 1:
        # Éste seria un caso con argumento no válido.
        print("No podemos calcular el término {0} de Fibonacci.".format(num))
    else:
        # El argumento está en el rango permitido
        print("El término {0} de Fibonacci es {1}.".format(num, fibonacci(num)))

prueba_fibonacci(3)        
prueba_fibonacci(4)
prueba_fibonacci(7)
prueba_fibonacci(40)
prueba_fibonacci(50)
