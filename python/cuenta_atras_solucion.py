"""
AUTOR: Willoom
FECHA: 30 de enero de 2025

Deseamos hacer un programa que realice por pantalla una cuenta atrás.

Pedirá al usuario un entero positivo, que hemos de comprobar.

Si no lo fuera, le informaremos y volveremos a solicitar el entero positivo.

Una vez tengamos el entero positivo, haremos una cuenta atrás desde el número introducido hasta el cero.

Al final, se imprimirá el mensaje "¡DESPEGUE!"

"""

# Solicitamos un entero positivo, mayor que cero, al usuario hasta que aporte un
# número válido.
número_válido = False
while not número_válido:
    número = int(input("Introduce un entero positivo, por favor: "))
    número_válido = número > 0
    if not número_válido:
        print("El número {0} no es un entero posivo.".format(número))
    
# En este punto tenemos un entero positivo en la variable número.

print("Iniciamos la cuenta atrás desde el {0}...".format(número))

# Vamos mostrando por pantalla la cuenta atrás.
# número se decrementa en uno en cada iteración y 
# termina el bucle cuando alcanza el valor cero
while número > 0:
    número -= 1
    print("...",número)
    
# Mostramos el mensaje final
print("¡DESPEGUE!")