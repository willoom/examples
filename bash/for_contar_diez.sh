#!/bin/bash

# AUTOR: Willoom
# 18 de diciembre de 2024

# Ejemplo con for
# Contar del 1 al 10 con un while

# En esta variable se irá acumulando la suma
contador=0

# Generamos una lista con los valores del uno al diez e iteramos 
# sobre sus elementos con la variable i
for i in `seq 10`; do
  # acumulamos el valor actual de iteración
  contador=$(($contador + $i))


  # mostramos el valor parcial calculado del acumulador
  echo "En la iteración $i llevamos acumulado $contador."

done

echo "La suma de los diez primeros naturales es $contador"
